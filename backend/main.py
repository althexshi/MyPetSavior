from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database.database import engine, Base  # Base should be the declarative base from SQLAlchemy
from database.models import PetDetails  # Ensure that PetDetails is defined in models.py
from database.db import get_db

# Initialize the database (creates tables if they don't exist)
Base.metadata.create_all(bind=engine)
app = FastAPI()

# Route to get a pet by ID
@app.get("/pets/{pet_id}")
def get_pet(pet_id: int, db: Session = Depends(get_db)):
    pet = db.query(PetDetails).filter(PetDetails.pet_id == pet_id).first()
    if pet is None:
        raise HTTPException(status_code=404, detail="Pet not found")
    return pet

# Route to create a new pet entry
@app.post("/pets/")
def create_pet(pet: PetDetails, db: Session = Depends(get_db)):
    db.add(pet)
    db.commit()
    db.refresh(pet)
    return pet

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

@app.get("/search")
async def search():
    return {"message": "Search results?"}

@app.get("/pet/{id}")
async def get_pet(id):
    return {"message": f"Pet: {id}"}


