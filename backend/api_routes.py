from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database.database import engine  # Base should be the declarative base from SQLAlchemy
from database.database import Base
from database.models import Animals  # Ensure that PetDetails is defined in models.py
from database.database import get_db

def add_api_routes(app: FastAPI):
    @app.get("/hello/{name}")
    async def say_hello(name: str):
        return {"message": f"Hello {name}"}

    @app.get("/search")
    async def search():
        return {"message": "Search results?"}

    # @app.get("/pets/{pet_id}")
    # def get_pet(pet_id: int, db: Session = Depends(get_db)):
    #     pet = db.query(Animals).filter(Animals.pet_id == pet_id).first()
    #     if pet is None:
    #         raise HTTPException(status_code=404, detail="Pet not found")
    #     return pet
    #
    # @app.post("/pets/")
    # def create_pet(pet: Animals, db: Session = Depends(get_db)):
    #     db.add(pet)
    #     db.commit()
    #     db.refresh(pet)
    #     return pet