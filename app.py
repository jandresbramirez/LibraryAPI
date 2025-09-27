from flask import Flask, jsonify
from controllers.author_controller import author_bp
from controllers.loan_controller import loan_bp
from controllers.book_controller import book_bp
from controllers.user_controller import user_bp

app = Flask(__name__) #Inicializamos Flask

# Configurar JWT
app.config['JWT_SECRET_KEY'] = JWT_SECRET_KEY
app.config['JWT_TOKEN_LOCATION'] = JWT_TOKEN_LOCATION
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = JWT_ACCESS_TOKEN_EXPIRES
app.config['JWT_HEADER_NAME'] = JWT_HEADER_NAME
app.config['JWT_HEADER_TYPE'] = JWT_HEADER_TYPE


app.register_blueprint(author_bp)
app.register_blueprint(loan_bp)
app.register_blueprint(book_bp)
app.register_blueprint(user_bp)

#Endpoint de bienvenida
@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Bienvenido a la API de LibraryAPI"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)