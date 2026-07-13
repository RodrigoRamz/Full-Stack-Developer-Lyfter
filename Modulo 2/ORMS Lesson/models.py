from typing import Optional

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "orm_users"

    id: Mapped[int] = mapped_column(primary_key=True)
    full_name: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )
    email: Mapped[str] = mapped_column(
        String(100),
        unique=True,
        nullable=False
    )

    addresses: Mapped[list["Address"]] = relationship(
        back_populates="user"
    )

    cars: Mapped[list["Car"]] = relationship(
        back_populates="user"
    )


class Address(Base):
    __tablename__ = "orm_addresses"

    id: Mapped[int] = mapped_column(primary_key=True)
    province: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )
    canton: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )
    exact_address: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )

    user_id: Mapped[int] = mapped_column(
        ForeignKey("orm_users.id"),
        nullable=False
    )

    user: Mapped["User"] = relationship(
        back_populates="addresses"
    )


class Car(Base):
    __tablename__ = "orm_cars"

    id: Mapped[int] = mapped_column(primary_key=True)
    brand: Mapped[str] = mapped_column(
        String(50),
        nullable=False
    )
    model: Mapped[str] = mapped_column(
        String(50),
        nullable=False
    )
    manufacturing_year: Mapped[int] = mapped_column(
        nullable=False
    )

    user_id: Mapped[Optional[int]] = mapped_column(
        ForeignKey("orm_users.id"),
        nullable=True
    )

    user: Mapped[Optional["User"]] = relationship(
        back_populates="cars"
    )