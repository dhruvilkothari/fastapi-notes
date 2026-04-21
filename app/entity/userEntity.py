from sqlalchemy import Column, Integer, String, Boolean

from app.db.database import Base
class User(Base):
    __tablename__ = "user"
    id:int = Column(Integer, primary_key=True, index=True)
    name: str =  Column(String, unique=True, index=True, nullable=False)
    email: str = Column(String)
    password: str = Column(String)
    age: int = Column(Integer)
    active: bool = Column(Boolean)
