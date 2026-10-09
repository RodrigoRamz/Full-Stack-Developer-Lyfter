from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import selectinload
from werkzeug.security import check_password_hash, generate_password_hash

from db import SessionLocal
from models import Invoice, InvoiceItem, Product, User


class UserRepository:

    def create_user(self, username, password, role="user"):
        with SessionLocal() as session:
            hashed_password = generate_password_hash(password)

            user = User(
                username=username,
                password=hashed_password,
                role=role
            )

            session.add(user)

            try:
                session.commit()
                session.refresh(user)
                return user

            except IntegrityError:
                session.rollback()
                return None

    def get_user(self, username, password):
        with SessionLocal() as session:
            statement = select(User).where(
                User.username == username,
            )

            user = session.execute(statement).scalar_one_or_none()

            if user is None:
                return None
            
            if not check_password_hash(user.password, password):
                return None
            
            return user

    def get_user_by_id(self, user_id):
        with SessionLocal() as session:
            return session.get(User, user_id)
        
        
class ProductRepository:

    def create_product(self, name, price, entry_date, quantity):
        with SessionLocal() as session:
            product = Product(
                name=name,
                price=price,
                entry_date=entry_date,
                quantity=quantity
            )

            session.add(product)

            try:
                session.commit()
                session.refresh(product)
                return product
            
            except IntegrityError:
                session.rollback()
                return None

    def get_all_products(self):
        with SessionLocal() as session:
            statement = select(Product)
            return session.execute(statement).scalars().all()

    def get_product_by_id(self, product_id):
        with SessionLocal() as session:
            return session.get(Product, product_id)

    def update_product(
        self,
        product_id,
        name=None,
        price=None,
        entry_date=None,
        quantity=None
    ):
        with SessionLocal() as session:
            product = session.get(Product, product_id)

            if product is None:
                return None, "Product not found"

            if name is not None:
                product.name = name

            if price is not None:
                product.price = price

            if entry_date is not None:
                product.entry_date = entry_date

            if quantity is not None:
                product.quantity = quantity

            try:
                session.commit()
                session.refresh(product)
                return product, None

            except IntegrityError:
                session.rollback()
                return None, "Invalid product data"
        
    def delete_product(self, product_id):
        with SessionLocal() as session:
            product = session.get(Product, product_id)

            if product is None:
                return False

            session.delete(product)
            session.commit()

            return True


class InvoiceRepository:

    def create_purchase(self, user_id, items):
        with SessionLocal() as session:
            user = session.get(User, user_id)

            if user is None:
                return None, "User not found"

            invoice = Invoice(
                user_id=user_id,
                total=0
            )

            session.add(invoice)
            session.flush()

            total = 0

            for item in items:
                if not isinstance(item, dict):
                    session.rollback()
                    return None, "Each item must be a JSON Object"
                
                required_fields =("product_id", "quantity")

                for field in required_fields:
                    if field not in item:
                        session.rollback()
                        return None, f"{field} is required for each item"
                    
                product_id = item["product_id"]
                requested_quantity = item["quantity"]

                product = session.get(Product, product_id)

                if product is None:
                    session.rollback()
                    return None, f"Product {product_id} not found"

                if requested_quantity <= 0:
                    session.rollback()
                    return None, "Quantity must be greater than zero"

                if product.quantity < requested_quantity:
                    session.rollback()
                    return None, f"Insufficient stock for product {product_id}"

                subtotal = product.price * requested_quantity

                invoice_item = InvoiceItem(
                    invoice_id=invoice.id,
                    product_id=product.id,
                    quantity=requested_quantity,
                    unit_price=product.price,
                    subtotal=subtotal
                )

                product.quantity -= requested_quantity
                total += subtotal

                session.add(invoice_item)

            invoice.total = total

            session.commit()
            session.refresh(invoice)

            return invoice, None    
        
    def get_invoice_by_id(self, invoice_id):
        with SessionLocal() as session:
            statement = (
                select(Invoice)
                .options(selectinload(Invoice.items))
                .where(Invoice.id == invoice_id)
            )

            return session.execute(statement).scalar_one_or_none()

    def get_invoices_by_user_id(self, user_id):
        with SessionLocal() as session:
            statement = (
                select(Invoice)
                .options(selectinload(Invoice.items))
                .where(Invoice.user_id == user_id)
                .order_by(
                    Invoice.purchase_date.desc(),
                    Invoice.id.desc()
                )
            )

            return session.execute(statement).scalars().all()