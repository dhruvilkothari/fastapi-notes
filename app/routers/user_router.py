from fastapi import APIRouter, Request, Response, Depends
from fastapi.responses import  JSONResponse
from sqlalchemy.orm import Session
from starlette import status
from app.dto.user import User, UserLogin
from app.responses.responses import send_success_response
from app.db.database import get_db
from app.service import user_service

router = APIRouter(
    prefix="/user",
    tags=["user"],
    responses={404: {"description": "Not found"}},

)

@router.post("/create" )
def create_user(req: Request, res: Response, user: User, db =  Depends(get_db)):

    return user_service.create_user(db, req, res,  user)

@router.get("/all")
def get_all_user(db: Session = Depends(get_db), offset: int = 0, limit: int = 100):
    return user_service.get_all_user(db, skip=offset, limit=limit)


@router.post("/login")
def login(req: Request, res: Response, user_login: UserLogin, db = Depends(get_db)):
    return user_service.login_user(req, res, user_login, db)