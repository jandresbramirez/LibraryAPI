from flask import Blueprint, request, jsonify
from services.author_service import AuthorService
from config.database import get_db_session

author_bp = Blueprint('author_bp', __name__)
service = AuthorService(get_db_session())

@author_bp.route('/authors', methods=['GET'])
def get_authors():
    authors = service.listar_autores()
    return jsonify([{'id': a.id, 'name': a.name} for a in authors]), 200

@author_bp.route('/authors/<int:author_id>', methods=['GET'])
def get_author(author_id):
    author = service.obtener_autor(author_id)
    if author:
        return jsonify({'id': author.id, 'name': author.name}), 200
    return jsonify({'error': 'Autor no encontrado'}), 404

@author_bp.route('/authors', methods=['POST'])
def create_author():
    data = request.get_json()
    name = data.get('name')
    if not name:
        return jsonify({'error': 'El nombre es obligatorio'}), 400
    author = service.crear_autor(name)
    return jsonify({'id': author.id, 'name': author.name}), 201

@author_bp.route('/authors/<int:author_id>', methods=['PUT'])
def update_author(author_id):
    data = request.get_json()
    name = data.get('name')
    author = service.actualizar_autor(author_id, name)
    if author:
        return jsonify({'id': author.id, 'name': author.name}), 200
    return jsonify({'error': 'Autor no encontrado'}), 404

@author_bp.route('/authors/<int:author_id>', methods=['DELETE'])
def delete_author(author_id):
    author = service.eliminar_autor(author_id)
    if author:
        return jsonify({'message': 'Autor eliminado'}), 200
    return jsonify({'error': 'Autor no encontrado'}), 404