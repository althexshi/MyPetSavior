from sqlalchemy import nullsfirst
from sqlalchemy.orm import Session
from database.database import SessionLocal, engine, Base
from database.models import Animals

Base.metadata.create_all(bind=engine)

def test_insert_pet(shelter, location, pet_name, breed, age, url_link, image_link, sex):
    db: Session = SessionLocal()
    try:
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

