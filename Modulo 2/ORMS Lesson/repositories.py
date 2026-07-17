from sqlalchemy import select
from sqlalchemy.orm import selectinload

from db import SessionLocal
from models import User, Car, Address


class UserRepository:
    def create_user(self, full_name, email):
        with SessionLocal() as session:
            user = User(
                full_name=full_name,
                email=email
            )

            session.add(user)
            session.commit()
            session.refresh(user)

            return user

    def update_user(self, user_id, full_name=None, email=None):
        with SessionLocal() as session:
            user = session.get(User, user_id)

            if user is None:
                return None

            if full_name is not None:
                user.full_name = full_name

            if email is not None:
                user.email = email

            session.commit()
            session.refresh(user)

            return user

    def delete_user(self, user_id):
        with SessionLocal() as session:
            user = session.get(User, user_id)

            if user is None:
                return False
            
            if user.addresses or user.cars:
                return False

            session.delete(user)
            session.commit()

            return True

    def get_all_users(self):
        with SessionLocal() as session:
            statement = select(User).options(
                selectinload(User.addresses),
                selectinload(User.cars)
            )

            result = session.execute(statement)

            return result.scalars().all()


class CarRepository:
    def create_car(self, brand, model, manufacturing_year):
        with SessionLocal() as session:
            car = Car(
                brand=brand,
                model=model,
                manufacturing_year=manufacturing_year
            )

            session.add(car)
            session.commit()
            session.refresh(car)

            return car

    def update_car(
        self,
        car_id,
        brand=None,
        model=None,
        manufacturing_year=None
    ):
        with SessionLocal() as session:
            car = session.get(Car, car_id)

            if car is None:
                return None

            if brand is not None:
                car.brand = brand

            if model is not None:
                car.model = model

            if manufacturing_year is not None:
                car.manufacturing_year = manufacturing_year

            session.commit()
            session.refresh(car)

            return car

    def delete_car(self, car_id):
        with SessionLocal() as session:
            car = session.get(Car, car_id)

            if car is None:
                return False

            session.delete(car)
            session.commit()

            return True

    def get_all_cars(self):
        with SessionLocal() as session:
            statement = select(Car).options(
                selectinload(Car.user)
            )

            result = session.execute(select(statement))
            return result.scalars().all()

    def assign_car_to_user(self, car_id, user_id):
        with SessionLocal() as session:
            car = session.get(Car, car_id)
            user = session.get(User, user_id)

            if car is None or user is None:
                return None

            car.user_id = user_id

            session.commit()
            session.refresh(car)

            return car


class AddressRepository:
    def create_address(self, province, canton, exact_address, user_id):
        with SessionLocal() as session:
            address = Address(
                province=province,
                canton=canton,
                exact_address=exact_address,
                user_id=user_id
            )

            session.add(address)
            session.commit()
            session.refresh(address)

            return address

    def update_address(
        self,
        address_id,
        province=None,
        canton=None,
        exact_address=None
    ):
        with SessionLocal() as session:
            address = session.get(Address, address_id)

            if address is None:
                return None

            if province is not None:
                address.province = province

            if canton is not None:
                address.canton = canton

            if exact_address is not None:
                address.exact_address = exact_address

            session.commit()
            session.refresh(address)

            return address

    def delete_address(self, address_id):
        with SessionLocal() as session:
            address = session.get(Address, address_id)

            if address is None:
                return False

            session.delete(address)
            session.commit()

            return True

    def get_all_addresses(self):
        with SessionLocal() as session:
            statement = select(Address).options(
                selectinload(Address.user)
            )
            result = session.execute(statement)
            
            return result.scalars().all()