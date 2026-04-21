from typing import Optional, TypeVar

from starlette import status

T = TypeVar("T")

class ApiResponse:
    status_code: int
    message: str
    data: Optional[T]
    class Config:
        json_schema_extra = {
            "example": {
                "data": {},
                "message": "success",
                "status_code": status.HTTP_200_OK,
            }
        }