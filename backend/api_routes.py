from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy import nullsfirst
from sqlalchemy.orm import Session
from database.database import SessionLocal, engine, Base, get_db
from database.models import Animals

def add_api_routes(app: FastAPI):
    @app.get("/api/search")
    def search_pets(query: str = None):

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

