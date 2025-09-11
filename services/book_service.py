from repositories.book_repository import BookRepository
from repositories.author_repository import AuthorRepository
from sqlalchemy.orm import Session

class BookService:
    """
    Capa de servicios para la gestión de usuarios
    """

    def __init__(self, db_session: Session):
        self.repository = BookRepository(db_session)
        self.author_repository = AuthorRepository(db_session)  

    # Obtener todos los libros
    def listar_libros(self):
        return self.repository.get_all_books()

    # Obtener un libro por su ID
    def obtener_libro_id(self, book_id: int):
        book = self.repository.get_book_by_id(book_id)
        if not book:
            raise ValueError("El libro no existe.")
        return book

    # Obtener todos los libros de un autor
    def obtener_libros_autor(self, author_id: int):
        autor = self.author_repository.get_author_by_id(author_id)
        if not autor:
            raise ValueError("El autor no existe.")
        return self.repository.get_books_by_author(author_id)

    # Crear un nuevo libro
    def crear_libro(self, title: str, author_id: int):
        # Validar que el autor exista
        autor = self.author_repository.get_author_by_id(author_id)
        if not autor:
            raise ValueError("El autor no existe, no se puede crear el libro.")

        # Validar que no exista un libro con el mismo título del mismo autor
        libros = self.repository.get_books_by_author(author_id)
        if any(l.title.lower() == title.lower() for l in libros):
            raise ValueError("Ese autor ya tiene un libro con ese título.")

        return self.repository.create_book(title, author_id)

    # Actualizar un libro existente
    def actualizar_libro(self, book_id: int, title: str = None, author_id: int = None):
        book = self.repository.get_book_by_id(book_id)
        if not book:
            raise ValueError("El libro no existe.")

        if author_id:
            autor = self.author_repository.get_author_by_id(author_id)
            if not autor:
                raise ValueError("El nuevo autor no existe.")

        if title:
            libros = self.repository.get_books_by_author(author_id or book.author_id)
            if any(l.title.lower() == title.lower() and l.id != book_id for l in libros):
                raise ValueError("Ya existe otro libro con ese título para este autor.")

        return self.repository.update_book(book_id, title, author_id)

    # Eliminar un libro por su ID
    def eliminar_libro(self, book_id: int):
        book = self.repository.get_book_by_id(book_id)
        if not book:
            raise ValueError("El libro no existe.")
        return self.repository.delete_book(book_id)