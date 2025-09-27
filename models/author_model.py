import datetime
from sqlalchemy import Column, Integer, String, ForeignKey, Date 
from sqlalchemy.orm import relationship
from models.db import Base

class Author(Base):
    __tablename__ = 'authors'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    
    #Relaciones entre tablas
    books = relationship('Book', back_populates='author', cascade="all, delete-orphan")