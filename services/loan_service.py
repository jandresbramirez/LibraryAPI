from repositories.book_repository import BookRepository
from repositories.user_repository import UserRepository
from repositories.loan_repository import LoanRepository
from sqlalchemy.orm import Session

class LoanService:
    """
    Capa de servicios para la gestión de usuarios
    """

    def __init__(self, db_session: Session):
        self.repository = LoanRepository(db_session)
        self.user_repository = UserRepository(db_session)
        self.book_repository = BookRepository(db_session)

    def listar_prestamos(self):
        return self.repository.get_all_loans()

    def obtener_prestamo_id(self, loan_id: int):
        loan = self.repository.get_loan_by_id(loan_id)
        if not loan:
            raise ValueError("El préstamo no existe.")
        return loan

    def crear_prestamo(self, user_id: int, book_id: int, loan_date=None, return_date=None):
        user = self.user_repository.get_user_by_id(user_id)
        if not user:
            raise ValueError("El usuario no existe.")
        book = self.book_repository.get_book_by_id(book_id)
        if not book:
            raise ValueError("El libro no existe.")
        loans = self.repository.get_all_loans()
        if any(l.book_id == book_id and l.return_date is None for l in loans):
            raise ValueError("Ese libro ya está prestado y no se ha devuelto.")

        return self.repository.create_loan(book_id, user_id, loan_date, return_date)

    def actualizar_prestamo(self, loan_id: int, return_date=None):
        loan = self.repository.get_loan_by_id(loan_id)
        if not loan:
            raise ValueError("El prestamo no existe.")
        if loan.return_date:
            raise ValueError("El préstamo ya fue devuelto.")

        return self.repository.update_loan(loan_id, return_date)

    def eliminar_prestamo(self, loan_id: int):
        loan = self.repository.get_loan_by_id(loan_id)
        if not loan:
            raise ValueError("El préstamo no existe.")
        return self.repository.delete_loan(loan_id)