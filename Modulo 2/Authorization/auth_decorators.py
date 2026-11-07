from functools import wraps

from flask import jsonify, request

from jwt_manager import JWTManager


def token_required(jwt_manager: JWTManager):
    def decorator(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            authorization_header = request.headers.get("Authorization")

            if not authorization_header:
                return jsonify(
                    error="Authorization header is required"
                ), 401

            if not authorization_header.startswith("Bearer "):
                return jsonify(
                    error="Authorization header must use Bearer token"
                ), 401

            token = authorization_header.replace("Bearer ", "", 1)

            decoded = jwt_manager.decode(token)

            if decoded is None:
                return jsonify(
                    error="Invalid or expired token"
                ), 401

            return function(decoded, *args, **kwargs)

        return wrapper

    return decorator


def role_required(jwt_manager: JWTManager, required_role):
    def decorator(function):
        @token_required(jwt_manager)
        @wraps(function)
        def wrapper(decoded, *args, **kwargs):
            if decoded.get("role") != required_role:
                return jsonify(error="Forbidden"), 403
            
            return function(decoded, *args, **kwargs)
        
        return wrapper
    
    return decorator