from sqlalchemy import nullsfirst
from sqlalchemy.orm import Session
from database.database import SessionLocal, engine, Base
from database.models import Animals

def insert_pet(shelter, location, pet_name, breed, age, url_link, image_link, sex):
    db: Session = SessionLocal()
    try:
        # Duplicate check (uses source_name which should match shelter parameter)
        existing_pet = db.query(Animals).filter(
            Animals.pet_name == pet_name,
            Animals.source_name == shelter  # Critical: Ensure shelter maps to source_name
        ).first()

        if existing_pet:
            print(f"Pet {pet_name} from {shelter} already exists. Skipping insert.")
            return

        new_pet = Animals(
            shelter_name = shelter,
            location = location,
            pet_name = pet_name,
            breed = breed,
            age = age,
            url_link = url_link,
            image_url = image_link,
            sex = sex,
        )
        db.add(new_pet)
        db.commit()
        print("Test pet inserted successfully!")
    except Exception as e:
        db.rollback()
        print(f"Error inserting test pet: {e}")
    finally:
        db.close()

