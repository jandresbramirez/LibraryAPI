from repositories.author_repository import AuthorRepository
from sqlalchemy.orm import Session

class AuthorService:
    """
    Capa de servicios para la gestión de usuarios
    """

    def __init__(self, db_session: Session):
        self.repository = AuthorRepository(db_session)

    #Obtener todos los autores
    def listar_autores(self):
        return self.repository.get_all_authors()

    #Obtener un autor por su ID
    def obtener_autor(self, author_id: int):
        author = self.repository.get_author_by_id(author_id)
        if not author:
            raise ValueError("El autor no existe.")
        return author

    #Crear un nuevo autor
    def crear_autor(self, name: str):
        autores = self.repository.get_all_authors()
        if any(a.name.lower() == name.lower() for a in autores):
            raise ValueError("Ya existe un autor con ese nombre.")
        return self.repository.create_author(name)

    #Actualizar un autor existente
    def actualizar_autor(self, author_id: int, name: str = None):
        author = self.repository.get_author_by_id(author_id)
        if not author:
            raise ValueError("El autor no existe.")

        if name:
            autores = self.repository.get_all_authors()
            if any(a.name.lower() == name.lower() and a.id != author_id for a in autores):
                raise ValueError("Ya existe otro autor con ese nombre.")

        return self.repository.update_author(author_id, name)

    #Eliminar un autor por su ID
    def eliminar_autor(self, author_id: int):
        author = self.repository.get_author_by_id(author_id)
        if not author:
            raise ValueError("El autor no existe.")
        return self.repository.delete_author(author_id)
    