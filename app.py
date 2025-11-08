from flask import Flask, jsonify
from config.jwt import *
from config.database import engine
from flask_jwt_extended import JWTManager
from models.db import Base
from controllers.author_controller import author_bp
from controllers.loan_controller import loan_bp
from controllers.book_controller import book_bp
from controllers.user_controller import user_bp, register_jwt_error_handlers
# Lista negra de tokens usados
from utils.blacklist import blacklist
# Importar CORS
from flask_cors import CORS

app = Flask(__name__) # Inicializamos Flask

# Configurar CORS para permitir solicitudes desde localhost:8000
# Configuración COMPLETA de CORS
cors = CORS(app, 
    resources={
        r"/*": {
            "origins": [
                "https://friendly-fortnight-5grgpwggr55f664-8000.app.github.dev",
                "http://localhost:8000",
                "http://127.0.0.1:8000",
                # Agrega otros origins si necesitas
            ],
            "methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"],
            "allow_headers": [
                "Content-Type", 
                "Authorization", 
                "Access-Control-Allow-Credentials",
                "X-Requested-With"
            ],
            "supports_credentials": True,
            "expose_headers": ["Content-Type", "Authorization"]
        }
    }
)

# Configurar JWT
app.config['JWT_SECRET_KEY'] = JWT_SECRET_KEY
app.config['JWT_TOKEN_LOCATION'] = JWT_TOKEN_LOCATION
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = JWT_ACCESS_TOKEN_EXPIRES
app.config['JWT_HEADER_NAME'] = JWT_HEADER_NAME
app.config['JWT_HEADER_TYPE'] = JWT_HEADER_TYPE

jwt = JWTManager(app)

app.register_blueprint(author_bp)
app.register_blueprint(loan_bp)
app.register_blueprint(book_bp)
app.register_blueprint(user_bp)

# Registrar manejadores personalizados de error JWT
register_jwt_error_handlers(app)

@jwt.token_in_blocklist_loader
def verify_token_in_blacklist(jwt_header, jwt_payload):
    return jwt_payload["jti"] in blacklist

# Si alguien usa un token bloqueado aparecerá este mensaje:
@jwt.revoked_token_loader
def revoked_token_callback(jwt_header, jwt_payload):
    return jsonify({"error": "El token ha sido revocado. Inicia sesión nuevamente."}), 401

# Endpoint de bienvenida
@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Bienvenido a la API de LibraryAPI"}), 200

if __name__ == "__main__":
    # Crear tablas automáticamente por si no se han creado en database.py
    print("Verificando y creando tablas de base de datos si es necesario...")
    Base.metadata.create_all(engine)
    print("Tablas creadas.")
    app.run(host="0.0.0.0", port=5000, debug=True)