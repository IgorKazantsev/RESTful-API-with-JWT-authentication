from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from datetime import datetime

from app.core.database import get_db
from app.models.log import Log
from app.schemas.log_schema import LogCreate, LogOut
from app.dependencies import require_admin, get_current_user

router = APIRouter(prefix="/logs", tags=["Logs"])

# Добавить лог (используется внутри других роутеров)
def create_log(action: str, user_id: int, db: Session):
    log = Log(action=action, user_id=user_id, timestamp=datetime.utcnow())
    db.add(log)
    db.commit()

# Получить все логи (только Admin)
@router.get("/", response_model=List[LogOut])
def get_logs(db: Session = Depends(get_db), current_admin = Depends(require_admin)):
    return db.query(Log).order_by(Log.timestamp.desc()).all()