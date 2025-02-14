from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import DeclarativeBase  # Fix import

# MySQL Database Connection URL
DATABASE_URL = "mysql+mysqlconnector://root:yourpassword@localhost/road_complaint"

# Create Engine
engine = create_engine(DATABASE_URL, echo=True)

# Session Local
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for models
class Base(DeclarativeBase):  # Fix declaration
    pass

