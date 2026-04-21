from typing import Any

from starlette import status


def send_success_response(data: Any, status_code: int = status.HTTP_200_OK):
    return {
        "data": data,
        "message": "success",
        "status_code": status_code,
    }

def send_failure_response(data: Any, status_code: int = status.HTTP_400_BAD_REQUEST):
    return {
        "data": data,
        "message": "failure",
        "status_code": status_code,
    }