from flask import Blueprint, request, jsonify
from services.user_service import UserService
from config.database import get_db_session

user_bp = Blueprint('user_bp', __name__)

# Instancia del servicio
service = UserService(get_db_session())

#Ruta GET para listar los usuarios en el sistema
@user_bp.route('/users', methods=['GET'])
def get_users():
    users = service.listar_usuarios()
    return jsonify([{'id': u.id, 'name': u.name, 'email': u.email} for u in users]), 200

#Ruta GET para listar un usuario por su ID
@user_bp.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = service.obtener_usuario_por_id(user_id)
    if user:
        return jsonify({'id': user.id, 'name': user.name, 'email': user.email}), 200
    return jsonify({'error': 'Usuario no encontrado'}), 404

#Ruta GET para listar un usuario por su correo
@user_bp.route('/users/<string:email>', methods=['GET'])
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
def update_user(user_id):
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    user = service.actualizar_usuario(user_id, name, email)
    if user:
        return jsonify({'id': user.id, 'name': user.name, 'email': user.email}), 200
    return jsonify({'error': 'Usuario no encontrado'}), 404

#Ruta DELETE para eliminar un usuario por su ID
@user_bp.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = service.eliminar_usuario(user_id)
    if user:
        return jsonify({'message': 'Usuario eliminado'}), 200
    return jsonify({'error': 'Usuario no encontrado'}), 404
