from fastapi import APIRouter, Request, Response, Depends
from fastapi.responses import  JSONResponse
from starlette import status
from app.dto.user import User
from app.responses.responses import send_success_response
from app.db.database import get_db

router = APIRouter(
    prefix="/user",
    tags=["user"],
    responses={404: {"description": "Not found"}},

)

@router.post("/create" )
def create_user(req: Request, res: Response, user: User, db =  Depends(get_db)):
    return JSONResponse(
        status_code=status.HTTP_201_CREATED,
        content= send_success_response(data=user.dict(), status_code=status.HTTP_201_CREATED),

    )