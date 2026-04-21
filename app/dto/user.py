from fastapi import HTTPException
from pydantic import BaseModel, Field, EmailStr, field_validator


class User(BaseModel):
    name: str = Field(min_length=5, max_length=50, description="User's name" )
    email: EmailStr
    password: str = Field(min_length=6, max_length=50, description="User's password")
    age: int = Field(ge=18, le= 80, description="User's age")
    active: bool = Field(default=True, description="User's active status")

    @field_validator("password")
    def validate_password(cls,  value: str):
        print(value)
        if "password" in value:
            raise HTTPException(status_code=400, detail="Select Strong Password")
        return value

    class Config:
        from_attributes = True
        json_schema_extra  = {
            "example": {
                "name": "",
                "email": "",
                "password": "",
                "age": 0,
                "active": False
            }
        }

class UserLogin(BaseModel):
    email: EmailStr
    password: str = Field(min_length=6, max_length=50, description="User's password")

    class Config:
        from_attributes = True