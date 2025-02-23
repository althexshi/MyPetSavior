from sqlalchemy.orm import Session
from database.database import SessionLocal, engine, Base
from database.models import PetDetails

Base.metadata.create_all(bind=engine)

def test_insert_pet():
    db: Session = SessionLocal()
    try:
        new_pet = PetDetails(
            shelter_name="Test Shelter",
            location="Test Location",
            pet_name="Test Pet",
            breed="Test Breed",
            age=2,
            behavior="Friendly",
            health_condition="Healthy",
            vaccination_status="vaccinated",
            pet_history="No known issues."
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
