from config.logger import logger
from flask import Blueprint, request, jsonify
from services.loan_service import LoanService
from config.database import get_db_session
from flask_jwt_extended import jwt_required
# Decorador para el manejo de roles
from config.roles_required import role_required

loan_bp = Blueprint('loan_bp', __name__)

# Instancia del servicio
service = LoanService(get_db_session())

#Ruta GET para listar los préstamos del sistema
@loan_bp.route('/loans', methods=['GET'])
@jwt_required()
@role_required(["admin", "editor"])
def get_loans():
    loans = service.listar_prestamos()
    return jsonify([{'id': loan.id, 'user_id': loan.user_id, 'book_id': loan.book_id, 'loan_date': loan.loan_date.isoformat(), 'return_date': loan.return_date.isoformat() if loan.return_date else None} for loan in loans]), 200

#Ruta GET para listar un préstamo por su ID
@loan_bp.route('/loans/<int:loan_id>', methods=['GET'])
@jwt_required()
@role_required(["admin", "editor"])
def get_loan(loan_id):
    loan = service.obtener_prestamo_id(loan_id)
    if loan:
        return jsonify({'id': loan.id, 'user_id': loan.user_id, 'book_id': loan.book_id, 'loan_date': loan.loan_date.isoformat(), 'return_date': loan.return_date.isoformat()}), 200
    return jsonify({'error': 'Préstamo no encontrado'}), 404

#Ruta POST para crear un nuevo préstamo
@loan_bp.route('/loans', methods=['POST'])
@jwt_required()
@role_required(["admin", "user"])
def create_loan():
    data = request.get_json()
    user_id = data.get('user_id')
    book_id = data.get('book_id')
    if not user_id or not book_id:
        return jsonify({'error': 'user_id y book_id son obligatorios'}), 400
    loan = service.crear_prestamo(user_id, book_id)
    return jsonify({'id': loan.id, 'user_id': loan.user_id, 'book_id': loan.book_id, 'loan_date': loan.loan_date.isoformat(), 'return_date': loan.return_date.isoformat() if loan.return_date else None}), 201

#Ruta PUT para actualizar la fecha de devolución de un préstamo por su ID
@loan_bp.route('/loans/<int:loan_id>', methods=['PUT'])
@jwt_required()
@role_required(["admin", "editor"])
def update_loan(loan_id):
    data = request.get_json()
    return_date = data.get('return_date')
    loan = service.actualizar_prestamo(loan_id, return_date)
    if loan:
        return jsonify({'id': loan.id, 'user_id': loan.user_id, 'book_id': loan.book_id, 'loan_date': loan.loan_date.isoformat(), 'return_date': loan.return_date.isoformat()}), 200
    return jsonify({'error': 'Préstamo no encontrado'}), 404

#Ruta DELETE para eliminar un prestamo por su ID
@loan_bp.route('/loans/<int:loan_id>', methods=['DELETE'])
@jwt_required()
@role_required(["admin", "editor"])
def delete_loan(loan_id):
    loan = service.eliminar_prestamo(loan_id)
    if loan:
        return jsonify({'message': 'Préstamo eliminado'}), 200
    return jsonify({'error': 'Préstamo no encontrado'}), 404