from config.logger import logger
from flask import Blueprint, request, jsonify
from services.book_service import BookService
from config.database import get_db_session
from flask_jwt_extended import jwt_required
# Decorador para el manejo de roles
from config.roles_required import role_required

book_bp = Blueprint('book_bp', __name__)

# Instancia del servicio
service = BookService(get_db_session())

#Ruta GET para listar los libros en el sistema
@book_bp.route('/books', methods=['GET'])
def get_books():
    books = service.listar_libros()
    return jsonify([{'id': b.id, 'title': b.title, 'author_id': b.author_id} for b in books]), 200

#Ruta GET para listar un libro por su ID
@book_bp.route('/books/<int:book_id>', methods=['GET'])
@jwt_required()
@role_required(["admin", "editor", "user"])
def get_book(book_id):
    book = service.obtener_libro_id(book_id)
    if book:
        return jsonify({'id': book.id, 'title': book.title, 'author_id': book.author_id}), 200
    return jsonify({'error': 'Libro no encontrado'}), 404

#Ruta GET para mostrar un libro por su id de autor
@book_bp.route('/books/<int:author_id>', methods=['GET'])
@jwt_required()
@role_required(["admin", "editor", "user"])
def get_book_author(author_id):
    author = service.obtener_libros_autor(author_id)
    if author:
        return jsonify({'id': book.id, 'title': book.title, 'author_id': book.author_id}), 200
    return jsonify({'error': 'Libro no encontrado'}), 404

#Ruta POST para crear un nuevo libro
@book_bp.route('/books', methods=['POST'])
@jwt_required()
@role_required(["admin", "editor"])
def create_book():
    data = request.get_json()
    title = data.get('title')
    author_id = data.get('author_id')
    if not title or not author_id:
        return jsonify({'error': 'Título y autor_id son obligatorios'}), 400
    book = service.crear_libro(title, author_id)
    return jsonify({'id': book.id, 'title': book.title, 'author_id': book.author_id}), 201

#Ruta PUT para actualizar un libro por su ID
@book_bp.route('/books/<int:book_id>', methods=['PUT'])
@jwt_required()
@role_required(["admin", "editor"])
def update_book(book_id):
    data = request.get_json()
    title = data.get('title')
    author_id = data.get('author_id')
    book = service.actualizar_libro(book_id, title, author_id)
    if book:
        return jsonify({'id': book.id, 'title': book.title, 'author_id': book.author_id}), 200
    return jsonify({'error': 'Libro no encontrado'}), 404

#Ruta DELETE para eliminar un libro por su ID
@book_bp.route('/books/<int:book_id>', methods=['DELETE'])
@jwt_required()
@role_required(["admin"])
def delete_book(book_id):
    book = service.eliminar_libro(book_id)
    if book:
        return jsonify({'message': 'Libro eliminado'}), 200
    return jsonify({'error': 'Libro no encontrado'}), 404
