from sqlalchemy import Column, Integer, String
from DBManager import Base


class Patient(Base):
    __tablename__ = "patient"

    patient_id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True)
    password = Column(String)
    name = Column(String)
    email = Column(String)
    dob = Column(String)

