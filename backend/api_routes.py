from fastapi import FastAPI, Depends, HTTPException, APIRouter
from sqlalchemy import nullsfirst
from sqlalchemy.orm import Session
from database.database import SessionLocal, engine, Base, get_db
from database.models import Animals
import asyncio

router = APIRouter()

@router.get("/api/search/{query}")
async def search_pets(query = None):
    print("Begin query")
    db: Session = SessionLocal()
    try:
        result = db.query(Animals.pet_name).all()
        pets = [row[0] for row in result]
        return pets
    except Exception as e:
        print(f"Error reading {e}")
        return None
    finally:
        db.close()

