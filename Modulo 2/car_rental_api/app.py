from flask import Flask, request

from db import PgManager
from repository import UserRepository, CarRepository, RentalRepository

app = Flask(__name__)

db_manager = PgManager(
    db_name="postgres",
    user="postgres",
    password="",
    host="localhost"
)

user_repository = UserRepository(db_manager)
car_repository = CarRepository(db_manager)
rental_repository = RentalRepository(db_manager)


def validate_required_fields(body, required_fields):
    if not body:
        return "Request body is required"

    for field in required_fields:
        if field not in body:
            return f"Missing required field: {field}"

    return None


@app.route("/")
def home():
    return {
        "message": "Car Rental API Running"
    }


@app.route("/users", methods=["GET"])
def get_users():
    filters = request.args.to_dict()
    return user_repository.get_all(filters)


@app.route("/users", methods=["POST"])
def create_user():
    body = request.get_json()

    error = validate_required_fields(
        body,
        ["full_name", "email", "username", "password", "birth_date"]
    )

    if error:
        return {"error": error}, 400

    user_id = user_repository.create(
        body["full_name"],
        body["email"],
        body["username"],
        body["password"],
        body["birth_date"],
        body.get("account_status", "active")
    )

    return {
        "message": "User created successfully",
        "user_id": user_id
    }, 201


@app.route("/users/<int:user_id>/status", methods=["PUT"])
def update_user_status(user_id):
    body = request.get_json()

    error = validate_required_fields(body, ["account_status"])

    if error:
        return {"error": error}, 400

    user_repository.update_status(
        user_id,
        body["account_status"]
    )

    return {
        "message": "User status updated successfully"
    }


@app.route("/users/<int:user_id>/delinquent", methods=["PUT"])
def flag_delinquent(user_id):
    user_repository.flag_delinquent(user_id)

    return {
        "message": "User flagged as delinquent successfully"
    }


@app.route("/cars", methods=["GET"])
def get_cars():
    filters = request.args.to_dict()
    return car_repository.get_all(filters)


@app.route("/cars", methods=["POST"])
def create_car():
    body = request.get_json()

    error = validate_required_fields(
        body,
        ["brand", "model", "manufacturing_year"]
    )

    if error:
        return {"error": error}, 400

    car_id = car_repository.create(
        body["brand"],
        body["model"],
        body["manufacturing_year"],
        body.get("car_status", "available")
    )

    return {
        "message": "Car created successfully",
        "car_id": car_id
    }, 201


@app.route("/cars/<int:car_id>/status", methods=["PUT"])
def update_car_status(car_id):
    body = request.get_json()

    error = validate_required_fields(body, ["car_status"])

    if error:
        return {"error": error}, 400

    car_repository.update_status(
        car_id,
        body["car_status"]
    )

    return {
        "message": "Car status updated successfully"
    }


@app.route("/rentals", methods=["GET"])
def get_rentals():
    filters = request.args.to_dict()
    return rental_repository.get_all(filters)


@app.route("/rentals", methods=["POST"])
def create_rental():
    body = request.get_json()

    error = validate_required_fields(
        body,
        ["user_id", "car_id", "returning_date"]
    )

    if error:
        return {"error": error}, 400

    rental_id = rental_repository.create(
        body["user_id"],
        body["car_id"],
        body["returning_date"],
        body.get("rental_status", "active")
    )

    return {
        "message": "Rental created successfully",
        "rental_id": rental_id
    }, 201


@app.route("/rentals/<int:rental_id>/status", methods=["PUT"])
def update_rental_status(rental_id):
    body = request.get_json()

    error = validate_required_fields(body, ["rental_status"])

    if error:
        return {"error": error}, 400

    rental_repository.update_status(
        rental_id,
        body["rental_status"]
    )

    return {
        "message": "Rental status updated successfully"
    }


@app.route("/rentals/<int:rental_id>/complete", methods=["PUT"])
def complete_rental(rental_id):
    result = rental_repository.complete_rental(rental_id)

    if not result:
        return {
            "error": "Rental not found"
        }, 404

    return {
        "message": "Rental completed successfully"
    }


if __name__ == "__main__":
    app.run(debug=True, port=8000)