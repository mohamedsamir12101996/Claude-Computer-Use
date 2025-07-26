from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.models import session as models
import uuid
import datetime

router = APIRouter()

class PromptRequest(BaseModel):
    session_id: str
    prompt: str

@router.post("/start-session")
def start_session(db: Session = Depends(get_db)):
    new_session = models.Session()
    db.add(new_session)
    db.commit()
    db.refresh(new_session)
    return {"session_id": new_session.id}

@router.post("/send")
def send_prompt(request: PromptRequest, db: Session = Depends(get_db)):
    msg = models.Message(
        session_id=request.session_id,
        role="user",
        content=request.prompt,
        timestamp=datetime.datetime.utcnow()
    )
    db.add(msg)
    db.commit()
    
    # TODO: integrate with agent, stream result back
    return {"message": f"Prompt received: {request.prompt}"}
