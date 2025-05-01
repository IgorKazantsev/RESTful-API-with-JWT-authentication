from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class CommentCreate(BaseModel):
    text: str
    book_id: int

class CommentOut(BaseModel):
    id: int
    text: str
    book_id: int
    user_id: int
    created_at: datetime

    class Config:
        orm_mode = True
