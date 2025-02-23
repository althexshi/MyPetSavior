from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

# Replace with your RDS connection string
SQLALCHEMY_DATABASE_URL = "mysql+mysqlconnector://admin:petsavior2025@petsavior-db.cbmo0ugqovpx.us-east-2.rds.amazonaws.com:3306/petsavior"

# Create an engine that knows how to connect to your RDS instance
engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)

# Create a session to interact with the database
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for models
Base = declarative_base()

# Base.metadata.create_all(bind=engine)

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()