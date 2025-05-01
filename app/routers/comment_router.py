from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from datetime import datetime

from app.core.database import get_db
from app.models.comment import Comment
from app.models.book import Book
from app.schemas.comment_schema import CommentCreate, CommentOut
from app.dependencies import require_user, get_current_user

router = APIRouter(prefix="/comments", tags=["Comments"])

# Добавить комментарий (только для зарегистрированных пользователей)
@router.post("/", response_model=CommentOut)
def add_comment(comment: CommentCreate, 
                db: Session = Depends(get_db), 
                current_user = Depends(require_user)):

    book = db.query(Book).filter(Book.id == comment.book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")

    new_comment = Comment(
        text=comment.text,
        book_id=comment.book_id,
        user_id=current_user.id,
        created_at=datetime.utcnow()
    )
    db.add(new_comment)
    db.commit()
    db.refresh(new_comment)
    return new_comment

# Получить все комментарии к книге
@router.get("/book/{book_id}", response_model=List[CommentOut])
def get_comments_for_book(book_id: int, db: Session = Depends(get_db)):
    return db.query(Comment).filter(Comment.book_id == book_id).all()
