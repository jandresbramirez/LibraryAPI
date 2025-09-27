import datetime
from sqlalchemy import Column, Integer, String, ForeignKey, Date 
from sqlalchemy.orm import relationship
from models.db import Base

class Book(Base):
    #Campos de la base de datos
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    author_id = Column(Integer, ForeignKey('authors.id'))

    #Relaciones entre tablas
    author = relationship('Author', back_populates="books")
    loans = relationship('Loan', back_populates="book", cascade="all, delete-orphan")