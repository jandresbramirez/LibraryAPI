from sqlalchemy.orm import Session
# from models.loan_model import Loan
from models.loan_model import Loan

class LoanRepository:

    """
    Repositorio para la gestión de prestamos en la base de datos
    integrando un CRUD.
    """

    def __init__(self, db_session: Session):
        self.db = db_session

    # Obtener todos los prestamos de la base de datos
    def get_all_loans(self):
        return self.db.query(Loan).all()

    # Obtener un prestamo en específico por un ID
    def get_loan_by_id(self, loan_id: int):
        return self.db.query(Loan).filter(Loan.id == loan_id).first()

    # Crear un nuevo prestamo
    def create_loan(self, book_id: int, user_id: int, loan_date=None, return_date=None):
        new_loan = Loan(
            book_id=book_id,
            user_id=user_id,
            loan_date=loan_date,
            return_date=return_date
        )
        self.db.add(new_loan)
        self.db.commit()
        self.db.refresh(new_loan)
        return new_loan

    # Actualizar la fecha de devolución de un prestamo existente
    def update_loan(self, loan_id: int, return_date=None):
        loan=self.get_loan_by_id(loan_id)
        if loan and return_date:
            loan.return_date=return_date
            self.db.commit()
            self.db.refresh(loan)
        return loan

    # Eliminar un prestamo por su ID
    def delete_loan(self, loan_id: int):
        loan = self.get_loan_by_id(loan_id)
        if loan:
            self.db.delete(loan)
            self.db.commit()
        return loan
