# backend/init_db.py
from sqlalchemy import inspect
from database.database import Base, engine

# Import your model definitions so SQLAlchemy registers them
import database.models  # this brings in Animals and Sources

def main():
    Base.metadata.create_all(bind=engine)
    insp = inspect(engine)
    print("Created tables:", insp.get_table_names())

if __name__ == "__main__":
    main()
