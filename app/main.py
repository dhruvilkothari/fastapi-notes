from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import uvicorn
from fastapi.exceptions import RequestValidationError
from starlette import status

from app.routers.user_router import router as user_router
from app.responses.responses import send_failure_response

app = FastAPI()


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    errors = []

    for err in exc.errors():
        errors.append({
            "field": err["loc"][-1],
            "message": err["msg"]
        })

    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content=send_failure_response(
            data=errors,
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY
        )
    )


app.include_router(user_router)


@app.get("/")
def test_route():
    return {"message": "Hello World"}


if __name__ == 'main':
    uvicorn.run(app, host="0.0.0.0", port=3000)
