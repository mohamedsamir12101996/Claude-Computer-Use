from fastapi import FastAPI
from app.api.routes import router as api_router
from app.websocket import router as ws_router
from fastapi.staticfiles import StaticFiles
from app.models import Session, Message

app = FastAPI()

app.include_router(api_router)
app.include_router(ws_router)

app.mount("/", StaticFiles(directory="static", html=True), name="static")