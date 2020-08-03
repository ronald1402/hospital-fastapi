import mysql.connector
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Zicare_dev",
    database="zihospital")

SQLALCHEMY_DATABASE_URL = "mysql+mysqlconnector://root:Zicare_dev@localhost:3306/zihospital"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()