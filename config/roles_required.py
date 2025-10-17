from flask_jwt_extended import get_jwt
from functools import wraps
from flask import jsonify

def role_required(roles):
    def decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            claims = get_jwt()
            user_role = claims.get("role")

            if user_role not in roles:
                return jsonify({
                    "error": f"Acceso denegado: se requiere uno de los roles {roles}"
                }), 403

            return fn(*args, **kwargs)
        return wrapper
    return decorator
