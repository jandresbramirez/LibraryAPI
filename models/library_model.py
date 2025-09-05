from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base

class Author(Base):
    __tablename__ = 'authors'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    books = relationship('Book', back_populates='author', cascade="all, delete-orphan")

class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    author_id = Column(Integer, ForeignKey('authors.id'))
    author = relationship('Author', back_populates="books", cascade="all, delete-orphan")
    loans = relationship('Loan', back_populates="book", cascade="all, delete-orphan")

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    
    #Relaciones entre tablas
    loans = relationship('Loan', back_populates="user", cascade="all, delete-orphan")

class Loan(Base):
    __tablename__ = "loans"
    id = Column(Integer, primary_key=True, index=True)
    book_id = Column(Integer, ForeignKey("books.id"))
    user_id = Column(Integer, ForeignKey("users.id"))
    loan_date = Column(Date, default=datetime.date.today)
    return_date = Column(Date, nullable=True)

    #Relaciones entre tablas
    book = relationship("Book", back_populates="loans")
    user = relationship("User", back_populates="loans")


