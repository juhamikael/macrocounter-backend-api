from sqlalchemy import Column, ForeignKey, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv

load_dotenv()
DATABASE_URL = os.getenv('DATABASE_URL')

engine = create_engine(DATABASE_URL)
sessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
Base = declarative_base()


class User(Base):
    __tablename__ = "userInfo"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(64))
    age = Column(Integer, default=18)
    height = Column(Integer, default=165)
    weight = Column(Integer, nullable=False, default=60)
    activity_level = Column(String(64))
    diet_style = Column(String(64))
    body_type = Column(String(64))
    gender = Column(String(64))


class ProcessedData(Base):
    __tablename__ = "userInfo"
    __table_args__ = {'extend_existing': True}
    bmr = Column(Integer)
    bmr7 = Column(Integer)
    bmi = Column(Float)
    daily_calories = Column(Integer)
    weekly_calories = Column(Integer)
    daily_protein = Column(Integer)
    daily_carbs = Column(Integer)
    daily_fat = Column(Integer)


class Food(Base):
    __tablename__ = "foods"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(64))
    protein = Column(Float)
    carbs = Column(Float)
    fat = Column(Float)
    calories = Column(Integer)


class FoodEaten(Base):
    __tablename__ = "food_eaten"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('userInfo.id'))
    food_id = Column(Integer, ForeignKey('foods.id'))
    food_name = Column(String(64))
    quantity = Column(Integer)
    protein = Column(Float)
    meal_type = Column(Integer)
    carbs = Column(Float)
    fat = Column(Float)
    calories = Column(Integer)
    time = Column(String(64))


Base.metadata.create_all(engine)
