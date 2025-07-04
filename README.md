# Building_ML_Platform 🤖

**Next‑Gen AI Agents Platform** 

Building_ML_Platform is a modular AI platform designed to prototype and evaluate intelligent agents capable of perception, reasoning, and action in real Linux server environments. 

This project serves as a sandbox for building and testing multi-agent systems that simulate real-world autonomy, coordination, and self-adaptation.

---

## 🧠 Project Overview

**Purpose**  
  Develop intelligent agents (voice, vision, decision-making, etc.) that interact within a real server-based environment using modular architecture.

**Inspired by**  
  - *Skynet* from **Terminator**  
  - *Hive* from **Resident Evil**

---

## 🚧 Repository Structure
~~~
Building_ML_Platform/
├── livekit-agent-python/     # Real‑time audio/video agent
├── RAG-voice-agent/          # Retrieval‑augmented voice agent
├── .gitignore
├── LICENSE                   # MIT License
└── README.md
~~~

---

## 🛠️ Getting Started

### 1. Clone the repo 
Create an SSH Private/Public key pair and add it to your GitHub account for easy git operations.
```bash
git clone git@github.com:harsh-rm/Building_ML_Platform.git
```
```
cd Building_ML_Platform
```
> **TL;DR:**  for https users  
> Origin: `https://github.com/user-name/repo-name.git`  
> Protocol: `https://`  
> Host: `github.com`  
> Default Port: `443`  
> User Id & Repo Path: `user-name/repo-name.git`

### 2. Create a virtual environment 
A virtual environment isolates your project’s Python packages from the system-wide Python installation, preventing version conflicts and keeping dependencies contained.
```
python3 -m venv .venv
```
```
source .venv/bin/activate
```

### 3. Install dependencies
```
pip install -r livekit-agent-python/requirements.txt \
            -r RAG-voice-agent/requirements.txt
```

### 4. Create your .env file(s)
Add your OpenAI, LiveKit, and/or other API keys here. Please keep them in stealth and do not --force push to GitHub.
```
cp RAG-voice-agent/.env.local RAG-voice-agent/.env
```

---

## 📦 Environment Management
Secrets: Store API keys in .env, and ensure .gitignore includes:  
```
.env
.venv
__pycache__
```  
Example template: Use .env.local to share variable structure without exposing sensitive values

---

## 📈 Roadmap
 Agent orchestration/orchestrator service
~~~
 Reinforcement learning / evolution engine

 Logging & monitoring subsystem

 CI/CD pipelines (GitHub Actions)

 Containerization via Docker / Kubernetes
~~~

---

## ▶️ Usage Examples
LiveKit Agent
```
cd livekit-agent-python
python3 assistant.py
```

RAG Voice Agent
```
cd RAG-voice-agent
python3 voice_agent.py
```

---
