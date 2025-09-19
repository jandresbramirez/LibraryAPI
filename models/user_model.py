import datetime
from sqlalchemy import Column, Integer, String, ForeignKey, Date 
from sqlalchemy.orm import relationship
from db import Base

class User(Base):
    #Campos de la base de datos
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    
    #Relaciones entre tablas
    loans = relationship('Loan', back_populates="user", cascade="all, delete-orphan")

"""
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True, nullable=False)
    password = Column(String(255), nullable=False)"""