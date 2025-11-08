# En el intérprete de Python:
from werkzeug.security import generate_password_hash
import sqlite3

conn = sqlite3.connect('library_local.db')
cursor = conn.cursor()

users = [
    ("Admin", "admin@test.com", generate_password_hash("admin123"), "admin"),
    ("Editor", "editor@test.com", generate_password_hash("editor123"), "editor"),
    ("Usuario", "user@test.com", generate_password_hash("user123"), "user")
]

for name, email, pwd, role in users:
    cursor.execute("INSERT OR IGNORE INTO users (name, email, password, role) VALUES (?, ?, ?, ?)", 
                   (name, email, pwd, role))
    print(f"Creado: {email}")

conn.commit()
conn.close()
print("Listo!")