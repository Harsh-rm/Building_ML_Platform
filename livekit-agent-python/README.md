# LiveKit Assistant

First, create a virtual environment, update pip, and install the required packages:

```
$ sudo apt update && sudo apt upgrade -y
$ sudo apt update
$ sudo apt install python3.12-venv -y
$ python -m venv .venv
$ source .venv/bin/activate
$ python -m pip install --upgrade pip
$ pip install livekit-agents[groq,silero,turn-detector]~=1.0rc
$ pip install python-dotenv
```

You need to set up the following environment variables:

```
LIVEKIT_URL=...
LIVEKIT_API_KEY=...
LIVEKIT_API_SECRET=...
GROQ_API_KEY=...
```

Then, run the assistant:

```
$ python assistant.py download-files
$ python assistant.py start
```

Finally, you can load the [hosted playground](https://agents-playground.livekit.io/) and connect it.

# Node Commands
```
$ rm -rf node_modules/.vite
$ rm -rf node_modules package-lock.json
$ npm cache clean --force
$ npm install
$ npm install --legacy-peer-deps
$ npm audit
$ 
```

