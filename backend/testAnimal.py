from sqlalchemy import nullsfirst
from sqlalchemy.orm import Session
from database.database import SessionLocal, engine, Base
from database.models import Animals

Base.metadata.create_all(bind=engine)

def test_insert_pet():
    db: Session = SessionLocal()
    try:
        new_pet = Animals(
            shelter_name = "Adopt Today!",
            location = "Fremont, CA",
            pet_name = "Joe",
            breed = "German Shepherd",
            age = 4,
            url_link = None,
            image_url = None,
            sex = "Female",
        )
        db.add(new_pet)
        db.commit()
        print("Test pet inserted successfully!")
    except Exception as e:
        db.rollback()
        print(f"Error inserting test pet: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    test_insert_pet()
