from flask import Blueprint, request, jsonify
from services.loan_service import LoanService
from config.database import get_db_session

loan_bp = Blueprint('loan_bp', __name__)

# Instancia del servicio
service = LoanService(get_db_session())

@loan_bp.route('/loans', methods=['GET'])
def get_loans():
    loans = service.listar_prestamos()
    return jsonify([{'id': l.id, 'user_id': l.user_id, 'book_id': l.book_id, 'loan_date': l.loan_date, 'return_date': l.return_date} for l in loans]), 200

@loan_bp.route('/loans/<int:loan_id>', methods=['GET'])
def get_loan(loan_id):
    loan = service.obtener_prestamo_id(loan_id)
    if loan:
        return jsonify({'id': loan.id, 'user_id': loan.user_id, 'book_id': loan.book_id, 'loan_date': loan.loan_date, 'return_date': loan.return_date}), 200
    return jsonify({'error': 'Préstamo no encontrado'}), 404

@loan_bp.route('/loans', methods=['POST'])
def create_loan():
    data = request.get_json()
    user_id = data.get('user_id')
    book_id = data.get('book_id')
    if not user_id or not book_id:
        return jsonify({'error': 'user_id y book_id son obligatorios'}), 400
    loan = service.crear_prestamo(user_id, book_id)
    return jsonify({'id': loan.id, 'user_id': loan.user_id, 'book_id': loan.book_id, 'loan_date': loan.loan_date, 'return_date': loan.return_date}), 201

@loan_bp.route('/loans/<int:loan_id>', methods=['PUT'])
def update_loan(loan_id):
    data = request.get_json()
    return_date = data.get('return_date')
    loan = service.actualizar_prestamo(loan_id, return_date)
    if loan:
        return jsonify({'id': loan.id, 'user_id': loan.user_id, 'book_id': loan.book_id, 'loan_date': loan.loan_date, 'return_date': loan.return_date}), 200
    return jsonify({'error': 'Préstamo no encontrado'}), 404

@loan_bp.route('/loans/<int:loan_id>', methods=['DELETE'])
def delete_loan(loan_id):
    loan = service.eliminar_prestamo(loan_id)
    if loan:
        return jsonify({'message': 'Préstamo eliminado'}), 200
    return jsonify({'error': 'Préstamo no encontrado'}), 404