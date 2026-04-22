
from fastapi import FastAPI, status, HTTPException, Request

import jwt
from datetime import datetime, timedelta, timezone

from starlette import status
from starlette.responses import JSONResponse

SECRET_KEY = "your-very-secret-key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def create_access_token(data: dict):
    to_encode = data.copy()
    # Set expiration timestamp
    expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    # Sign and encode the token
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def verify_token(req: Request):
    try:
        token = req.headers.get("authorization")
        if not token:
            return  JSONResponse(
                status_code=status.HTTP_401_UNAUTHORIZED,
                content={
                    "message": "Authentication credentials were not provided."
                }
            )
        token = token.split(" ")[1]


        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return payload
    except jwt.ExpiredSignatureError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
        )
