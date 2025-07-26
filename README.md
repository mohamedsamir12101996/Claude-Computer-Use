# Claude AI Agent Backend - FastAPI + Docker

> Coding Challenge Submission for CambioML Senior Backend/DevOps Engineer Role  
> Built by: Mohamed Samir

---

## 🚀 Overview

This project replaces the experimental Streamlit interface from [Anthropic's demo](https://github.com/anthropics/anthropic-quickstarts/tree/main/computer-use-demo) with a production-ready backend using **FastAPI**, **Docker**, **PostgreSQL**, and **WebSockets**.

### Features

- Session management APIs
- Real-time streaming with WebSocket
- Persistent chat history (PostgreSQL)
- Simple frontend (HTML/JS)
- Claude agent integration
- (Optional) VNC/Guacamole

---

## 🛠️ Stack

- FastAPI
- WebSocket
- SQLAlchemy (PostgreSQL)
- Docker & Docker Compose
- HTML + JS
- (Optional) Apache Guacamole for VNC
- (Optional) Anthropic Claude agent

---

## 📂 Project Structure

project_root/
├── app/
│ ├── main.py
│ ├── api/routes.py
│ ├── websocket.py
│ ├── services/agent_runner.py
│ ├── models/session.py
│ └── db/database.py
├── static/index.html
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md


---

## 🧪 Running Locally

### Prerequisites

- Docker & Docker Compose

### Steps

```bash
# Clone project and enter directory
git clone https://github.com/mohamedsamir12101996/Claude-Computer-Use
cd Claude-Computer-Use

# Run services
docker-compose up --build

| Method | Endpoint           | Description                  |
| ------ | ------------------ | ---------------------------- |
| POST   | `/start-session`   | Creates new session          |
| POST   | `/send`            | Sends prompt to Claude agent |
| WS     | `/ws/{session_id}` | Real-time updates WebSocket  |
