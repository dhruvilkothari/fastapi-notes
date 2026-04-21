from fastapi import Request
from psycopg2._psycopg import List
from sqlalchemy.orm import Session

from app.dto.user import User
from app.entity.userEntity import User



def create_user_db(db, req: Request, user: User):
    user_entity = User(
        **user.dict(),
    )
    db.add(user_entity)
    db.commit()
    db.refresh(user_entity)
    return user_entity


def get_all_user_db(db: Session, skip: int = 0, limit: int = 100):
    li = db.query(User).offset(skip).limit(limit).all()
    return li
