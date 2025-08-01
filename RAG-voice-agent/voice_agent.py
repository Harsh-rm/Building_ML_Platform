import logging
import os
from dotenv import load_dotenv
from livekit.agents import JobContext, JobProcess, WorkerOptions, cli
from livekit.agents.job import AutoSubscribe
from livekit.agents.llm import (
    ChatContext,
)
from livekit.agents.pipeline import VoicePipelineAgent
from livekit.plugins import cartesia, silero, llama_index, assemblyai

load_dotenv(dotenv_path=".env")

logger = logging.getLogger("voice-assistant")
from llama_index.llms.ollama import Ollama
from llama_index.core import (
    SimpleDirectoryReader,
    StorageContext,
    VectorStoreIndex,
    load_index_from_storage,
    Settings
)
from llama_index.core.chat_engine.types import ChatMode
from llama_index.embeddings.huggingface import HuggingFaceEmbedding

load_dotenv()  

#pip install --upgrade llama-index

embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-small-en-v1.5")
llm=Ollama(model="gemma3", request_timeout=120.0)
Settings.llm = llm
Settings.embed_model = embed_model

# check if storage already exists
PERSIST_DIR = "./chat-engine-storage"
if not os.path.exists(PERSIST_DIR):
    # load the documents and create the index
    documents = SimpleDirectoryReader("Documents").load_data()
    index = VectorStoreIndex.from_documents(documents)
    # store it for later
    index.storage_context.persist(persist_dir=PERSIST_DIR)
else:
    # load the existing index
    storage_context = StorageContext.from_defaults(persist_dir=PERSIST_DIR)
    index = load_index_from_storage(storage_context)


def prewarm(proc: JobProcess):
    proc.userdata["vad"] = silero.VAD.load()


async def entrypoint(ctx: JobContext):
    chat_context = ChatContext().append(
        role="system",
        text=(
            "You are a funny, witty assistant."
            "Respond with short and concise answers. Avoid using unpronouncable punctuation or emojis."
        ),
    )
    
    chat_engine = index.as_chat_engine(chat_mode=ChatMode.CONTEXT)
    logger.info(f"Connecting to room {ctx.room.name}")
   
    await ctx.connect(auto_subscribe=AutoSubscribe.AUDIO_ONLY)
   
    participant = await ctx.wait_for_participant()
    logger.info(f"Starting voice assistant for participant {participant.identity}")
    
    stt_impl = assemblyai.STT()
    agent = VoicePipelineAgent(
        vad=ctx.proc.userdata["vad"],
        stt=stt_impl,
        llm=llama_index.LLM(chat_engine=chat_engine),
        tts=cartesia.TTS(
            model="sonic-2",
            voice="794f9389-aac1-45b6-b726-9d9369183238",
        ),
        chat_ctx=chat_context,
    )

    agent.start(ctx.room, participant)

    await agent.say(
        "Hey there! How can I help you today?",
        allow_interruptions=True,
    )


if __name__ == "__main__":
    print("Starting voice agent...")
    cli.run_app(
        WorkerOptions(
            entrypoint_fnc=entrypoint,
            prewarm_fnc=prewarm,
        ),
    )