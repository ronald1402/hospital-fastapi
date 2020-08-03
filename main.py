import uvicorn
from fastapi import FastAPI, Depends
from pydantic.main import BaseModel
from sqlalchemy.orm import Session

import Models
import Schema
from AccountController import loginController, updateController, createController
from DBManager import engine, SessionLocal

Models.Base.metadata.create_all(bind=engine)

app = FastAPI()


class LoginRequest(BaseModel):
    username: str
    password: str


class UpdateRequest(BaseModel):
    username: str
    password: str
    name: str
    email: str


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/login")
def logins(loginRequest: Schema.UserLoginRequest, db: Session = Depends(get_db)):
    return loginController(db, loginRequest)

@app.post("/create")
def logins(createRequest: Schema.UserCreateRequest, db: Session = Depends(get_db)):
    return createController(db, createRequest)


@app.put("/update")
def updateAccount(updateRequest: Schema.UserUpdateRequest, db: Session = Depends(get_db)):
    return updateController(db, updateRequest)


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8080)