from config.logger import logger
from flask import Blueprint, request, jsonify
from services.user_service import UserService
from config.database import get_db_session
from flask_jwt_extended import create_access_token, jwt_required, JWTManager
# Handler personalizado para errores de autenticación JWT
from flask_jwt_extended.exceptions import NoAuthorizationError
from flask import current_app
# Decorador para el manejo de roles
from config.roles_required import role_required

user_bp = Blueprint('user_bp', __name__)

# Instancia del servicio
service = UserService(get_db_session())


# Controlador de mensajes de error en autenticación
def register_jwt_error_handlers(app):
    @app.errorhandler(NoAuthorizationError)
    def handle_no_auth_error(e):
        logger.warning("Intento de acceso sin autenticación JWT")
        return jsonify({'error': 'Usuario no autenticado. Debe logearse/registrarse para acceder a este apartado.'}), 401, {'Content-Type': 'application/json; charset=utf-8'}


#--------------------ENDPOINTS--------------------#

#Ruta POST para el login de usuarios
@user_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        logger.warning("Login fallido: usuario o contraseña no proporcionados")
        return jsonify({'error': 'Email y contraseña son obligatorios'}), 400
    user = service.authenticate_user(email, passord)
    if user:
        access_token = create_access_token(identity=str(user.id), additional_claims={"role": user.role})
        logger.info(f"Usuario autenticado: {email}")
        return jsonify({'access_token': access_token}), 200
    logger.warning(f"Login fallido para el usuario: {email} | Credenciales inválidas")
    return jsonify({'error': 'Credenciales inválidas'}), 401

#Ruta POST para cerrar sesión
@user_bp.route('/logout', methods=['POST'])
@jwt_required()
def logout():
    """
    Endpoint para cerrar sesión del usuario actual.
    El token JWT utilizado se marca como inválido (revocado).
    """
    jti = get_jwt()["jti"]  # Identificador único del token
    blacklist.add(jti)
    return jsonify({"message": "Sesión cerrada correctamente"}), 200

#Ruta GET para listar los usuarios en el sistema
@user_bp.route('/users', methods=['GET'])
@jwt_required()
@role_required(["admin"])
def get_users():
    users = service.listar_usuarios()
    return jsonify([{'id': u.id, 'name': u.name, 'email': u.email} for u in users]), 200

#Ruta GET para listar un usuario por su ID
@user_bp.route('/users/<int:user_id>', methods=['GET'])
@jwt_required()
@role_required(["admin", "editor"])
def get_user(user_id):
    user = service.obtener_usuario_por_id(user_id)
    if user:
        return jsonify({'id': user.id, 'name': user.name, 'email': user.email}), 200
    return jsonify({'error': 'Usuario no encontrado'}), 404

#Ruta GET para listar un usuario por su correo
@user_bp.route('/users/<string:email>', methods=['GET'])
@jwt_required()
@role_required(["admin", "editor"])
def get_user_email(email):
    user_email = service.obtener_usuario_por_email(email)
    if user_email:
        return jsonify({'id': user_email.id, 'name': user_email.name, 'email': user_email.email}), 200
    return jsonify({'error': 'Correo no encontrado'}), 404

#Ruta POST para crear un nuevo usuario
@user_bp.route('/registry', methods=['POST'])
def create_user():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    password = data.get('password')
    if not name or not email or not password:
        return jsonify({'error': 'Nombre, correo y contraseña son obligatorios'}), 400
    user = service.crear_usuario(name, email, password)
    return jsonify({'id': user.id, 'name': user.name, 'email': user.email, 'password': user.password}), 201

#Ruta PUT para actualizar un usuario por su ID
@user_bp.route('/users/<int:user_id>', methods=['PUT'])
@jwt_required()
@role_required(["admin", "editor"])
def update_user(user_id):
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    password = data.get('password')
    user = service.actualizar_usuario(user_id, name, email, password)
    if user:
        return jsonify({'id': user.id, 'name': user.name, 'email': user.email}), 200
    return jsonify({'error': 'Usuario no encontrado'}), 404

#Ruta DELETE para eliminar un usuario por su ID
@user_bp.route('/users/<int:user_id>', methods=['DELETE'])
@jwt_required()
@role_required(["admin"])
def delete_user(user_id):
    user = service.eliminar_usuario(user_id)
    if user:
        return jsonify({'message': 'Usuario eliminado'}), 200
    return jsonify({'error': 'Usuario no encontrado'}), 404
