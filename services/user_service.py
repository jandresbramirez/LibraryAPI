from config.logger import logger
from repositories.user_repository import UserRepository
from sqlalchemy.orm import Session
from werkzeug.security import generate_password_hash, check_password_hash

class UserService:
    """
    Capa de servicios para la gestión de usuarios
    """

    def __init__(self, db_session: Session):
        self.repository = UserRepository(db_session)

    #Función para autenticar las credenciales del usuario, haciendo uso de el repositorio de get_user_by_email
    def authenticate_user(self, email: str, password: str):
        user = self.repository.get_user_by_email(email)
        if not user:
            logger.warning(f"Usuario no encontrado con el email: {email}")
            return None

        if not check_password_hash(user.password, password):
            logger.warning(f"Contraseña incorrecta para el usuario: {email}")
            return None
        logger.info(f"Usuario {email} autenticado correctamente.")
        return user


    #Listar todos los usuarios de la base de datos
    def listar_usuarios(self):
        return self.repository.get_all_users()

    #Obtener usuario por su ID
    def obtener_usuario_por_id(self, user_id: int):
        user = self.repository.get_user_by_id(user_id)
        if not user:
            raise ValueError("El usuario no existe.")
        return user

    #Obtener usuario por su correo
    def obtener_usuario_por_email(self, email: str):
        user_email = self.repository.get_user_by_email(email)
        if not user_email:
            raise ValueError("El email no existe.")
        return user_email

    #Crear un nuevo usuario en el sistema
    def crear_usuario(self, name: str, email: str, password: str, role: str = 'user'):
        users = self.repository.get_all_users()
        if any(u.email == email for u in users):
            raise ValueError("El email ya está registrado.")
        password_hashed = generate_password_hash(password)
        return self.repository.create_user(name, email, password_hashed, role)

    #Actualizar un usuario por su ID
    def actualizar_usuario(self, user_id: int, name: str = None, email: str = None):
        user = self.repository.get_user_by_id(user_id)
        if not user:
            raise ValueError("El usuario no existe.")
        if email:
            users = self.repository.get_all_users()
            if any(u.email == email and u.id != user_id for u in users):
                raise ValueError("Ese email ya está en uso por otro usuario.")
        if password:
            password_hashed = generate_password_hash(password)

        return self.repository.update_user(user_id, name, email, password_hashed)

    #Eliminar un usuario de la base de datos por su ID
    def eliminar_usuario(self, user_id: int):
        user = self.repository.get_user_by_id(user_id)
        if not user:
            raise ValueError("El usuario no existe.")
        return self.repository.delete_user(user_id)