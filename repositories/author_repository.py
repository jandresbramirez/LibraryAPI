from sqlalchemy.orm import Session
from models.library_model import Author

class AuthorRepository:

    """
    Repositorio para la gestión de autores en la base de datos
    integrando un CRUD.
    """

    def __init__(self, db_session: Session):
        self.db = db_session

    #Obtiene todos los autores en la base de datos
    def get_all_authors(self):
        return self.db.query(Author).all()

    #Obtiene un autor por su ID
    def get_author_by_id(self, author_id: int):
        return self.db.query(Author).filter(Author.id == author_id).first()

    #Crea un nuevo autor
    def create_author(self, name: str):
        new_author = Author(name = name)
        self.db.add(new_author)
        self.db.commit()
        self.db.refresh(new_author)
        return new_author

    #Actualiza el nombre de un actor por su ID
    def update_author(self, author_id: int, name: str = None):
        author = self.get_author_by_id(author_id)
        if author and name:
            author.name = name
            self.db.commit()
            self.db.refresh(author)
        return author
    
    #Elimina un autor por su ID
    def delete_author(self, author_id: int):
        author = self.get_author_by_id(author_id)
        if author:
            self.db.delete(author)
            self.db.commit()
        return author

    