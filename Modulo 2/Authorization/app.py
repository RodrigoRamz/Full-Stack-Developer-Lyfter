from pathlib import Path
from datetime import date
import json

from flask import Flask, jsonify, request

from jwt_manager import JWTManager
from repositories import InvoiceRepository, ProductRepository, UserRepository
from auth_decorators import role_required, token_required
from cache import cache_manager

app = Flask("authorization-service")

user_repository = UserRepository()
product_repository = ProductRepository()
invoice_repository = InvoiceRepository()

BASE_DIR = Path(__file__).resolve().parent

jwt_manager = JWTManager(
    BASE_DIR / "keys" / "private_key.pem",
    BASE_DIR / "keys" / "public_key.pem"
)


@app.route("/liveness")
def liveness():
    return jsonify(
        message="Authorization service is running"
    ), 200


@app.route("/register", methods=["POST"])
def register():
    data = request.get_json(silent=True)

    if not data:
        return jsonify(error="JSON body is required"), 400

    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return jsonify(
            error="Username and password are required"
        ), 400

    user = user_repository.create_user(
        username=username,
        password=password,
        role="user"
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
        ), 401

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
@token_required(jwt_manager)
def me(decoded):
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


@app.route("/products", methods=["POST"])
@role_required(jwt_manager, "admin")
def create_product(decoded):
    data = request.get_json(silent=True)

    if not data:
        return jsonify(error="JSON body is required"), 400

    required_fields = [
        "name",
        "price",
        "entry_date",
        "quantity"
    ]

    for field in required_fields:
        if field not in data:
            return jsonify(
                error=f"{field} is required"
            ), 400

    try:
        entry_date = date.fromisoformat(data["entry_date"])
    except (TypeError, ValueError):
        return jsonify(
            error="entry_date must use YYYY-MM-DD format"
        ), 400

    product = product_repository.create_product(
        name=data["name"],
        price=data["price"],
        entry_date=entry_date,
        quantity=data["quantity"]
    )

    if product is None:
        return jsonify(
            error="Invalid product data"
        ), 400

    return jsonify(
        product={
            "id": product.id,
            "name": product.name,
            "price": float(product.price),
            "entry_date": str(product.entry_date),
            "quantity": product.quantity
        }
    ), 201


@app.route("/products", methods=["GET"])
@role_required(jwt_manager, "admin")
def get_products(decoded):
    products = product_repository.get_all_products()

    return jsonify(
        products=[
            {
                "id": product.id,
                "name": product.name,
                "price": float(product.price),
                "entry_date": str(product.entry_date),
                "quantity": product.quantity
            }
            for product in products
        ]
    ), 200

@app.route("/products/<int:product_id>", methods=["GET"])
@role_required(jwt_manager, "admin")
def get_product(decoded, product_id):
    cache_key = f"product:{product_id}"

    cached_product = cache_manager.get_data(cache_key)

    if cached_product is not None:
        return jsonify(product=json.loads(cached_product)), 200

    product = product_repository.get_product_by_id(product_id)

    if product is None:
        return jsonify(error="Product not found"), 404

    product_data = {
        "id": product.id,
        "name": product.name,
        "price": float(product.price),
        "entry_date": str(product.entry_date),
        "quantity": product.quantity
    }

    cache_manager.store_data(
        cache_key,
        json.dumps(product_data),
        time_to_live=300
    )

    return jsonify(product=product_data), 200


@app.route("/products/<int:product_id>", methods=["PUT"])
@role_required(jwt_manager, "admin")
def update_product(decoded, product_id):
    data = request.get_json(silent=True)

    if not data:
        return jsonify(error="JSON body is required"), 400

    if "entry_date" in data:
        try:
            data["entry_date"] = date.fromisoformat(
                data["entry_date"]
            )
        except (TypeError, ValueError):
            return jsonify(
                error="entry_date must use YYYY-MM-DD format"
            ), 400

    product, error = product_repository.update_product(
        product_id=product_id,
        name=data.get("name"),
        price=data.get("price"),
        entry_date=data.get("entry_date"),
        quantity=data.get("quantity")
    )

    if error == "Product not found":
        return jsonify(error=error), 404

    if error:
        return jsonify(error=error), 400
    
    cache_manager.delete_data(f"product:{product_id}")

    return jsonify(
        product={
            "id": product.id,
            "name": product.name,
            "price": float(product.price),
            "entry_date": str(product.entry_date),
            "quantity": product.quantity
        }
    ), 200


@app.route("/products/<int:product_id>", methods=["DELETE"])
@role_required(jwt_manager, "admin")
def delete_product(decoded, product_id):
    deleted = product_repository.delete_product(product_id)

    if not deleted:
        return jsonify(error="Product not found"), 404
    
    cache_manager.delete_data(f"product:{product_id}")

    return jsonify(
        message="Product deleted successfully"
    ), 200


@app.route("/purchases", methods=["POST"])
@token_required(jwt_manager)
def create_purchase(decoded):
    data = request.get_json(silent=True)

    if not data:
        return jsonify(error="JSON body is required"), 400

    user_id = decoded.get("id")
    items = data.get("items")

    if user_id is None:
        return jsonify(
            error="Token does not contain a user ID"
        ), 401

    if not items:
        return jsonify(
            error="items are required"
        ), 400

    invoice, error = invoice_repository.create_purchase(
        user_id=user_id,
        items=items
    )

    if error:
        return jsonify(error=error), 400

    return jsonify(
        invoice={
            "id": invoice.id,
            "user_id": invoice.user_id,
            "purchase_date": str(invoice.purchase_date),
            "total": float(invoice.total)
        }
    ), 201


@app.route("/invoices/<int:invoice_id>", methods=["GET"])
@token_required(jwt_manager)
def get_invoice(decoded, invoice_id):
    invoice = invoice_repository.get_invoice_by_id(invoice_id)

    if invoice is None:
        return jsonify(error="Invoice not found"), 404

    if (
        decoded.get("role") != "admin"
        and invoice.user_id != decoded.get("id")
    ):
        return jsonify(error="Forbidden"), 403

    return jsonify(
        invoice={
            "id": invoice.id,
            "user_id": invoice.user_id,
            "purchase_date": str(invoice.purchase_date),
            "total": float(invoice.total),
            "items": [
                {
                    "product_id": item.product_id,
                    "quantity": item.quantity,
                    "unit_price": float(item.unit_price),
                    "subtotal": float(item.subtotal)
                }
                for item in invoice.items
            ]
        }
    ), 200


@app.route("/invoices", methods=["GET"])
@token_required(jwt_manager)
def get_user_invoices(decoded):
    user_id = decoded.get("id")

    if user_id is None:
        return jsonify(
            error="Token does not contain a user ID"
        ), 401

    invoices = invoice_repository.get_invoices_by_user_id(
        user_id
    )

    return jsonify(
        invoices=[
            {
                "id": invoice.id,
                "user_id": invoice.user_id,
                "purchase_date": str(invoice.purchase_date),
                "total": float(invoice.total),
                "items": [
                    {
                        "product_id": item.product_id,
                        "quantity": item.quantity,
                        "unit_price": float(item.unit_price),
                        "subtotal": float(item.subtotal)
                    }
                    for item in invoice.items
                ]
            }
            for invoice in invoices
        ]
    ), 200


if __name__ == "__main__":
    app.run(debug=True, port=8000)