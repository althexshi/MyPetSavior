from sqlalchemy import Column, Integer, String, Text, Enum, TIMESTAMP
from sqlalchemy.sql import func
# from database.database import Base
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

class PetDetails(Base):
    __tablename__ = 'pet_details'

    pet_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    shelter_name = Column(String(255), nullable=False)
    location = Column(String(255), nullable=False)
    pet_name = Column(String(255), nullable=False)
    breed = Column(String(100), nullable=True)
    age = Column(Integer, nullable=True)
    behavior = Column(Text, nullable=True)
    health_condition = Column(String(255), nullable=True)
    vaccination_status = Column(Enum('vaccinated', 'not_vaccinated', 'pending'), default='pending')
    pet_history = Column(Text, nullable=True)
    created_at = Column(TIMESTAMP, server_default=func.current_timestamp())
