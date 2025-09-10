from sqlalchemy.orm import Session
from models.library_model import Book

class BookRepository:

    """
    Repositorio para la gestión de libros en la base de datos
    integrando un CRUD.
    """

    def __init__(self, db_session: Session):
        self.db = db_session

    def get_all_books(self):
        return self.db.query(Book).all()

    def get_book_by_id(self, book_id: int):
        return self.db.query(Book).filter(Book.id = book_id).first()

    def get_books_by_author(self, author_id: int):
        return self.db.query(Book).filter(Book.author_id = author_id).all()

    def create_book(self, title: str, author_id: int):
        new_book = Book(title=title, author_id=author_id)
        self.db.add(new_book)
        self.db.commit()
        self.db.refresh(new_book)
        return new_book

    def update_book(self, book_id: int, title: str = None, author_id: int = None):
        book = self.get_book_by_id(book_id)
        if book:
            if title:
                book.title = title
            if author_id:
                book.author_id = author_id
            self.db.commit()
            self.db.refresh(book)
        return book

    def delete_book(self, book_id: int):
        book = self.get_book_by_id(book_id)
        if book:
            self.db.delete(book)
            self.db.commit()
        return book