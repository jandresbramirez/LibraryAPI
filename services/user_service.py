from repositories.user_repository import UserRepository
from sqlalchemy.orm import Session

class UserService:
    """
    Capa de servicios para la gestión de usuarios
    """

    def __init__(self, db_session: Session):
        self.repository = UserRepository(db_session)

    def listar_usuarios(self):
        return self.repository.get_all_users()

    def obtener_usuario_id(self, user_id: int):
        user = self.repository.get_user_by_id(user_id)
        if not user:
            raise ValueError("El usuario no existe.")
        return user

    def obtener_usuario_email(self, email: str):
        email = self.repository.get_user_by_email(email)
        if not email:
            raise ValueError("El email no existe.")
        return email

    def crear_usuario(self, name: str, email: str):
        users = self.repository.get_all_users()
        if any(u.email == email for u in users):
            raise ValueError("El email ya está registrado.")
        return self.repository.create_user(name, email)

    def actualizar_usuario(self, user_id: int, name: str = None, email: str = None):
        user = self.repository.get_user_by_id(user.id)
        if not user:
            raise ValueError("El usuario no existe.")
        if email:
            users = self.repository.get_all_users()
            if any(u.email == email and u.id != user_id for u in users):
                raise ValueError("Ese email ya está en uso por otro usuario.")

        return self.repository.update_user(user_id, name, email)

    def eliminar_usuario(self, user_id: int):
        user = self.repository.get_user_by_id(user_id)
        if not user:
            raise ValueError("El usuario no existe.")
        return self.repository.delete_user(user_id)