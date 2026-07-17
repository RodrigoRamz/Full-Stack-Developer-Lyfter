from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DB_URI = "postgresql://postgres:postgres@localhost:5432/postgres"

engine = create_engine(DB_URI, echo=True)

SessionLocal = sessionmaker(bind=engine)