from db import PgManager
from repository import UserRepository, CarRepository, RentalRepository


db_manager = PgManager(
    db_name="postgres",
    user="postgres",
    password="",
    host="localhost"
)

user_repository = UserRepository(db_manager)

users = user_repository.get_all()

print(users)

car_repository = CarRepository(db_manager)

cars = car_repository.get_all()

print(cars)

rental_repository = RentalRepository(db_manager)

rentals = rental_repository.get_all()

print(rentals)

db_manager.close_connection()