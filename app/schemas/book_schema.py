from pydantic import BaseModel
from typing import Optional

# Для создания книги
class BookCreate(BaseModel):
    title: str
    author: str
    description: Optional[str] = None

# Для обновления книги
class BookUpdate(BaseModel):
    title: Optional[str] = None
    author: Optional[str] = None
    description: Optional[str] = None

# Для вывода книги
class BookOut(BaseModel):
    id: int
    title: str
    author: str
    description: Optional[str] = None

    class Config:
        orm_mode = True
