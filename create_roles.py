# create_roles.py
from config.database import get_db_session
from models.user_model import User
from models.loan_model import Loan
from models.book_model import Book
from models.author_model import Author
from services.user_service import UserService

from werkzeug.security import generate_password_hash  # 👈 importa esta función

db = get_db_session()
service = UserService(db)

def create_initial_users():
    # Verificar si ya existen
    admin_exists = db.query(User).filter_by(email="admin@example.com").first()
    editor_exists = db.query(User).filter_by(email="editor@example.com").first()

    if admin_exists and editor_exists:
        print("✅ Los usuarios admin y editor ya existen. Nada que hacer.")
        return

    # Crear admin
    if not admin_exists:
        admin = User(
            name="Administrador",
            email="admin@example.com",
            password=generate_password_hash("admin123"),  # 👈 aquí el cambio
            role="admin"
        )
        db.add(admin)
        print("🟢 Usuario admin creado: admin@example.com / admin123")

    # Crear editor
    if not editor_exists:
        editor = User(
            name="Editor",
            email="editor@example.com",
            password=generate_password_hash("editor123"),  # 👈 igual aquí
            role="editor"
        )
        db.add(editor)
        print("🟢 Usuario editor creado: editor@example.com / editor123")

    db.commit()
    print("✅ Proceso finalizado con éxito.")
    
if __name__ == "__main__":
    create_initial_users()
