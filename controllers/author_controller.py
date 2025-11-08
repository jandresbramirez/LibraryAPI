from config.logger import logger
from flask import Blueprint, request, jsonify
from services.author_service import AuthorService
from config.database import get_db_session
from flask_jwt_extended import jwt_required
# Decorador para el manejo de roles
from config.roles_required import role_required

author_bp = Blueprint('author_bp', __name__)

service = AuthorService(get_db_session())

#Ruta GET para listar autores
@author_bp.route('/authors', methods=['GET'])
def get_authors():
    authors = service.listar_autores()
    return jsonify([{'id': a.id, 'name': a.name} for a in authors]), 200

#Ruta GET para listar autor por su ID
@author_bp.route('/authors/<int:author_id>', methods=['GET'])
@jwt_required()
@role_required(["admin", "editor", "user"])
def get_author(author_id):
    author = service.obtener_autor(author_id)
    if author:
        return jsonify({'id': author.id, 'name': author.name}), 200
    return jsonify({'error': 'Autor no encontrado'}), 404

#Ruta POST para crear un nuevo autor
@author_bp.route('/authors', methods=['POST'])
@jwt_required()
@role_required(["admin", "editor", "user"])
def create_author():
    data = request.get_json()
    name = data.get('name')
    if not name:
        return jsonify({'error': 'El nombre es obligatorio'}), 400
    author = service.crear_autor(name)
    return jsonify({'id': author.id, 'name': author.name}), 201

#Ruta PUT para actualizar un autor por su ID
@author_bp.route('/authors/<int:author_id>', methods=['PUT'])
@jwt_required()
@role_required(["admin", "editor"])
def update_author(author_id):
    data = request.get_json()
    name = data.get('name')
    author = service.actualizar_autor(author_id, name)
    if author:
        return jsonify({'id': author.id, 'name': author.name}), 200
    return jsonify({'error': 'Autor no encontrado'}), 404

#Ruta DELETE para eliminar un autor por su ID
@author_bp.route('/authors/<int:author_id>', methods=['DELETE'])
@jwt_required()
@role_required(["admin"])
def delete_author(author_id):
    author = service.eliminar_autor(author_id)
    if author:
        return jsonify({'message': 'Autor eliminado'}), 200
    return jsonify({'error': 'Autor no encontrado'}), 404