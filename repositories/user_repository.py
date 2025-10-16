from sqlalchemy.orm import Session
# from models.user_model import User
from models.user_model import User
class UserRepository:

    """
    Repositorio para la gestión de usuarios en la base de datos
    integrando un CRUD.
    """

    def __init__(self, db_session: Session):
        self.db = db_session

    #Obtener todos los usuarios de la base de datos
    def get_all_users(self):
        return self.db.query(User).all()

    #Obtener un usuario en específico por un ID
    def get_user_by_id(self, user_id: int):
        return self.db.query(User).filter(User.id == user_id).first()

    #Obtener un usuario en específico por email
    def get_user_by_email(self, email: str):
        return self.db.query(User).filter(User.email == email).first()

    #Crear un nuevo usuario
    def create_user(self, name: str, email: str, password: str, role: str):
        new_user = User(name = name, email = email, password = password, role = role)
        self.db.add(new_user)
        self.db.commit()
        self.db.refresh(new_user)
        return new_user

    #Actualizar nombre y/o correo de un usuario por su ID.
    def update_user(self, user_id: int, name: str = None, email: str = None, password: str = None):
        user = self.get_user_by_id(user_id)
        if user:
            if name:
                user.name = name
            if email:
                user.email = email
            if password:
                user.password = password
            self.db.commit()
            self.db.refresh(user)
        return user

    #Eliminar un usuario por su ID
    def delete_user(self, user_id: int):
        user = self.get_user_by_id(user_id)
        if user:
            self.db.delete(user)
            self.db.commit()
        return user

