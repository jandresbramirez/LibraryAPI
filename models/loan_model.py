import datetime
from sqlalchemy import Column, Integer, String, ForeignKey, Date 
from sqlalchemy.orm import relationship
from models.db import Base

class Loan(Base):
    #Campos de la base de datos
    __tablename__ = "loans"
    id = Column(Integer, primary_key=True, index=True)
    book_id = Column(Integer, ForeignKey("books.id"))
    user_id = Column(Integer, ForeignKey("users.id"))
    loan_date = Column(Date, default=datetime.date.today)
    return_date = Column(Date, nullable=True)

    #Relaciones entre tablas
    book = relationship("Book", back_populates="loans")
    user = relationship("User", back_populates="loans")