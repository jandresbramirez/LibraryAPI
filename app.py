from flask import Flask
from controllers.author_controller import author_bp
from controllers.loan_controller import loan_bp
from controllers.book_controller import book_bp
from controllers.user_controller import user_bp

app = Flask(__name__)

app.register_blueprint(author_bp)
app.register_blueprint(loan_bp)
app.register_blueprint(book_bp)
app.register_blueprint(user_bp)

if __name__ == "__main__":
    app.run(host"0.0.0.0", port=5000, debug=True)