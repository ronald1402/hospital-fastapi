from pydantic import BaseModel


class UserLoginRequest(BaseModel):
    username: str
    password: str


class UserCreateRequest(UserLoginRequest):
    name: str
    email: str


class UserUpdateRequest(UserLoginRequest):
    name: str
    email: str

    class Config:
        orm_mode = True
