from pydantic import BaseModel
from datetime import datetime

class LogCreate(BaseModel):
    action: str
    user_id: int

class LogOut(BaseModel):
    id: int
    action: str
    user_id: int
    timestamp: datetime

    class Config:
        orm_mode = True
