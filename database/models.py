from sqlalchemy import Column, Integer, String, Text, Enum, TIMESTAMP
from sqlalchemy.sql import func
from database.database import Base

class Animals(Base):
    __tablename__ = 'animals'

    pet_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    shelter_name = Column(String(255), nullable=False)
    location = Column(String(255), nullable=False)
    pet_name = Column(String(255), nullable=False)
    breed = Column(String(100), nullable=True)
    age = Column(Integer, nullable=True)
    url_link = Column(String(255), nullable=True)
    image_url = Column(String(255), nullable=True)
    sex = Column(Enum('Male', 'Female', 'Unknown'), nullable=True)
    created_at = Column(TIMESTAMP, server_default=func.current_timestamp())
