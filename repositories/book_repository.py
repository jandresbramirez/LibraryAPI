from sqlalchemy.orm import Session
from models.library_model import Book

class BookRepository:

    """
    Repositorio para la gestión de libros en la base de datos
    integrando un CRUD.
    """

    def __init__(self, db_session: Session):
        self.db = db_session

    #Obtener todos los libros de la base de datos
    def get_all_books(self):
        return self.db.query(Book).all()

    #Obtener un libro en específico por un ID
    def get_book_by_id(self, book_id: int):
        return self.db.query(Book).filter(Book.id == book_id).first()

    #Obtener un libro en específico por un Autor
    def get_books_by_author(self, author_id: int):
        return self.db.query(Book).filter(Book.author_id == author_id).all()

    #Crear un nuevo prestamo
    def create_book(self, title: str, author_id: int):
        new_book = Book(title=title, author_id=author_id)
        self.db.add(new_book)
        self.db.commit()
        self.db.refresh(new_book)
        return new_book

    #Actualizar titulo y/o autor de un libro por un ID
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

    #Eliminar un libro por su ID
    def delete_book(self, book_id: int):
        book = self.get_book_by_id(book_id)
        if book:
            self.db.delete(book)
            self.db.commit()
        return book