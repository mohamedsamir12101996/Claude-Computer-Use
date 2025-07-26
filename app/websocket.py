from fastapi import APIRouter, WebSocket, WebSocketDisconnect
import asyncio

router = APIRouter()

connections = {}

@router.websocket("/ws/{session_id}")
async def stream_progress(websocket: WebSocket, session_id: str):
    await websocket.accept()
    if session_id not in connections:
        connections[session_id] = []
    connections[session_id].append(websocket)

    try:
        for i in range(5):
            await websocket.send_text(f"Update {i+1} for session {session_id}")
            await asyncio.sleep(1)
        await websocket.send_text("✅ Done.")
    except WebSocketDisconnect:
        connections[session_id].remove(websocket)
        await websocket.close()
