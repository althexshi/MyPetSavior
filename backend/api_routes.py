from fastapi import FastAPI, Depends, HTTPException, APIRouter, Query
from sqlalchemy.orm import Session
from database.database import SessionLocal, get_db
from database.models import Animals
from sqlalchemy import and_

router = APIRouter()

@router.get("/api/search/{query}/{sex}/{breed}/{min_age}/{max_age}/{species}")
async def search_pets(
    query = None,
    sex = None,
    breed = None,
    min_age: int | None = Query(None),
    max_age: int | None = Query(None),
    species = None
):
    print("Begin query")
    db: Session = SessionLocal()
    try:
        q = db.query(Animals)

        # Filter by pet name starting with the query
        if query:
            q = q.filter(Animals.pet_name.ilike(f"{query}%"))  # Case-insensitive search

        # Other filters
        if sex:
            q = q.filter(Animals.sex == sex)
        if breed:
            q = q.filter(Animals.breed == breed)
        if min_age is not None:
            q = q.filter(Animals.age >= min_age)
        if max_age is not None:
            q = q.filter(Animals.age <= max_age)
        if species:
            q = q.filter(Animals.source_name == species)

        results = q.all()
        return [{
            "pet_id": animal.pet_id,
            "name": animal.pet_name,
            "breed": animal.breed,
            "age": animal.age,
            "sex": animal.sex,
            "location": animal.location,
            "image_url": animal.image_url
        } for animal in results]

    except Exception as e:
        print(f"Error: {e}")
        raise HTTPException(status_code=500, detail="Database error")
    finally:
        db.close()

def add_api_routes(app: FastAPI):
    app.include_router(router)