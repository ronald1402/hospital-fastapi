from sqlalchemy.orm import Session
import Models, Schema
import bcrypt


def get_user_by_username(db: Session, username: str):
    return db.query(Models.Patient).filter(Models.Patient.username == username).first()


def login(db: Session, user: Schema.UserLoginRequest):
    return db.query(Models.Patient).filter(Models.Patient.username == user.username,
                                           Models.Patient.password == user.password).first()

def checkExistingUsername(db: Session, user: Schema.UserCreateRequest):
    return db.query(Models.Patient).filter(Models.Patient.username == user.username).first()


def create_user(db: Session, user: Schema.UserCreateRequest):
    hashed_password = bcrypt.hashpw(user.password.encode('utf-8'), bcrypt.gensalt())

    db_user = Models.Patient(username=user.username, password=hashed_password, name=user.name, email=user.email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def update_user(db: Session, user_request: Schema.UserUpdateRequest):
    user = db.query(Models.Patient).filter(Models.Patient.username == user_request.username).first()
    setattr(user, 'name', user_request.name)
    setattr(user, 'email', user_request.email)
    db.commit()
    userUpdate = Models.Patient(username=user.username, name=user.name, email=user.email)

    return userUpdate
