import re

from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session

from AccountService import login, update_user, create_user, checkExistingUsername
from DBManager import SessionLocal
from MessageType import MessageType
from Result import Result

import Schema


def get_db(self):
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def loginController(db: Session, loginRequest: Schema.UserLoginRequest):
    if not validateLoginRequest(loginRequest.username, loginRequest.password):
        return Result(MessageType.getMessageDetail(MessageType.INVALID_PARAM), None)
    isExistUser = login(db, loginRequest)
    if isExistUser is None:
        return Result(MessageType.getMessageDetail(MessageType.AUTHENTICATION_FAILED), None)
    return Result(MessageType.getMessageDetail(MessageType.SUCCESS), loginRequest.username)

def updateController(db: Session, updateRequest: Schema.UserUpdateRequest):
    if not validateUpdateRequest(updateRequest):
        return Result(MessageType.getMessageDetail(MessageType.INVALID_PARAM), None)
    if not validateEmail(updateRequest.email):
        return Result(MessageType.getMessageDetail(MessageType.EMAIL_NOT_VALID), None)
    isExistUser = login(db, updateRequest)
    if isExistUser is None:
        return Result(MessageType.getMessageDetail(MessageType.AUTHENTICATION_FAILED), None)
    userUpdate = update_user(db, updateRequest)
    return Result(MessageType.getMessageDetail(MessageType.SUCCESS), userUpdate)

def createController(db: Session, createRequest: Schema.UserCreateRequest):
    if not validateUpdateRequest(createRequest):
        return Result(MessageType.getMessageDetail(MessageType.INVALID_PARAM), None)
    if not validateEmail(createRequest.email):
        return Result(MessageType.getMessageDetail(MessageType.EMAIL_NOT_VALID), None)
    isExistUser = checkExistingUsername(db, createRequest)
    if isExistUser is not None:
        return Result(MessageType.getMessageDetail(MessageType.USER_EXISTED), None)
    userCreate = create_user(db, createRequest)
    return Result(MessageType.getMessageDetail(MessageType.SUCCESS), userCreate)


"""
Validation in login :
-   Username and password mandatory
-   Both of them must alphanumeric
"""
def validateLoginRequest(username, password):
    if len(username) == 0 or len(password) == 0:
        return False
    if not username.isalnum() or not password.isalnum():
        return False
    else:
        return True

"""
Validation in update :
-   Username, password, name and email mandatory
-   Both of them must alphanumeric except email 
-   validation in alphanumeric include no whitespace in string
"""

def validateUpdateRequest(request):
    if not validateLoginRequest(request.name, request.password):
        return False
    if len(request.name) == 0 or len(request.email) == 0 or not request.name.isalnum():
        return False
    else:
        return True

def validateEmail(email):
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    if (not re.search(regex, email)) or len(email) == 0:
        return False
    else:
        return True

