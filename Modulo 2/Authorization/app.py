from pathlib import Path

from flask import Flask, jsonify, request

from jwt_manager import JWTManager
from repositories import UserRepository


app = Flask("authorization-service")

user_repository = UserRepository()

BASE_DIR = Path(__file__).resolve().parent

jwt_manager = JWTManager(
    BASE_DIR / "keys" / "private_key.pem",
    BASE_DIR / "keys" / "public_key.pem"
)


@app.route("/liveness")
def liveness():
    return jsonify(message="Authorization service is running"), 200


@app.route("/register", methods=["POST"])
def register():
    data = request.get_json(silent=True)

    if not data:
        return jsonify(error="JSON body is required"), 400

    username = data.get("username")
    password = data.get("password")
    role = data.get("role", "user")

    if not username or not password:
        return jsonify(
            error="Username and password are required"
        ), 400

    if role not in ("admin", "user"):
        return jsonify(
            error="Role must be 'admin' or 'user'"
        ), 400

    user = user_repository.create_user(
        username=username,
        password=password,
        role=role
    )

    if user is None:
        return jsonify(
            error="Username already exists"
        ), 409

    token = jwt_manager.encode(
        {
            "id": user.id,
            "role": user.role
        }
    )

    if token is None:
        return jsonify(
            error="Token could not be created"
        ), 500

    return jsonify(
        token=token,
        user={
            "id": user.id,
            "username": user.username,
            "role": user.role
        }
    ), 201


@app.route("/login", methods=["POST"])
def login():
    data = request.get_json(silent=True)

    if not data:
        return jsonify(error="JSON body is required"), 400

    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return jsonify(
            error="Username and password are required"
        ), 400

    user = user_repository.get_user(
        username=username,
        password=password
    )

    if user is None:
        return jsonify(
            error="Invalid username or password"
        ), 403

    token = jwt_manager.encode(
        {
            "id": user.id,
            "role": user.role
        }
    )

    if token is None:
        return jsonify(
            error="Token could not be created"
        ), 500

    return jsonify(
        token=token,
        user={
            "id": user.id,
            "username": user.username,
            "role": user.role
        }
    ), 200


@app.route("/me", methods=["GET"])
def me():
    authorization_header = request.headers.get("Authorization")

    if not authorization_header:
        return jsonify(
            error="Authorization header is required"
        ), 403

    if not authorization_header.startswith("Bearer "):
        return jsonify(
            error="Authorization header must use Bearer token"
        ), 403

    token = authorization_header.replace("Bearer ", "", 1)

    decoded = jwt_manager.decode(token)

    if decoded is None:
        return jsonify(
            error="Invalid or expired token"
        ), 403

    user_id = decoded.get("id")

    if user_id is None:
        return jsonify(
            error="Token does not contain a user ID"
        ), 403

    user = user_repository.get_user_by_id(user_id)

    if user is None:
        return jsonify(
            error="User not found"
        ), 404

    return jsonify(
        id=user.id,
        username=user.username,
        role=user.role
    ), 200

if __name__ == "__main__":
    app.run(debug=True, port=8000)