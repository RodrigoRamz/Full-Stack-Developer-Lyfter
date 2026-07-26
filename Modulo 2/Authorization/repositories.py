from sqlalchemy import select
from sqlalchemy.exc import IntegrityError

from db import SessionLocal
from models import User


class UserRepository:

    def create_user(self, username, password, role="user"):
        with SessionLocal() as session:
            user = User(
                username=username,
                password=password,
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
                User.password == password
            )

            return session.execute(statement).scalar_one_or_none()

    def get_user_by_id(self, user_id):
        with SessionLocal() as session:
            return session.get(User, user_id)