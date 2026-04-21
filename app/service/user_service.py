from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from starlette import status
from fastapi import Request, Response
from app.responses.responses import  send_success_response, send_failure_response
from app.dto.user import User, UserLogin
from app.entity.userEntity import User as UserEntity
from app.repository.user_repo import  create_user_db
from app.repository.user_repo import  get_all_user_db, get_user_by_email
from sqlalchemy.exc import IntegrityError
from app.security.hash_password import  get_password_hash, verify_password

def create_user(db, req: Request, res: Response, user: User):
    try:
        new_password = get_password_hash(user.password)
        user.password =  new_password
        user_entity = create_user_db(db, req, user)
        return send_success_response(user_entity)

    except IntegrityError as e:
        p  = str(e.orig)
        p = p.split(":")[-1]
        data_val = p.split(".")[-1]
        print(p)
        db.rollback()  # VERY IMPORTANT
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content=send_failure_response(
                data= data_val,
            )
        )

    except Exception as e:
        db.rollback()
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={
                "status_code": status.HTTP_500_INTERNAL_SERVER_ERROR,
                "message": "Something went wrong",
                "error": str(e)  # keep for debugging (remove in production)
            }
        )

def get_all_user(db: Session, skip: int = 0, limit: int = 100):

    return get_all_user_db(db, skip=skip, limit=limit)

def login_user(req: Request, res: Response, user_login: UserLogin, db: Session):
    email = user_login.email
    password = user_login.password

    user_entity: UserEntity = get_user_by_email(db, email)
    print(user_entity)
    if not user_entity:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content=send_failure_response(
                data= "User not found",
            )
        )
    flag = verify_password(password, user_entity.password)
    if not flag:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content=send_failure_response(
                data="User not found",
            )
        )
    return send_success_response(
        user_entity
    )



