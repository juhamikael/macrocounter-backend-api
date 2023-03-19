from sqlalchemy.orm import Session
from schemas import FoodUpdate
import models
from fastapi import HTTPException


def update_macros(update_food, request: FoodUpdate, db: Session):
    # #Update Food Info
    update_food.protein = request.protein
    update_food.carbs = request.carbs
    update_food.fat = request.fat
    update_food.calories = update_food.protein * 4 + update_food.carbs * 4 + update_food.fat * 9
    db.commit()


def update_name(update_food, request, db: Session):
    update_food.name = request.name
    db.commit()


def add_and_commit(model, db: Session):
    db.add(model)
    db.commit()
    db.refresh(model)


def post_food(request, db: Session):
    last_food = db.query(models.Food).order_by(models.Food.id.desc()).first()
    new_id = last_food.id + 1 if last_food else 1
    new_food = models.Food(
        id=new_id,
        name=request.name,
        protein=request.protein,
        carbs=request.carbs,
        fat=request.fat,
        calories=request.carbs * 4 + request.fat * 9 + request.protein * 4
    )
    query = db.query(models.Food).filter(models.Food.id == new_id).first()
    query_name = db.query(models.Food).filter(models.Food.name == request.name).first()
    if query:
        raise HTTPException(status_code=400, detail="Food already exists")
    elif query_name is not None:
        add_and_commit(new_food, db)
        return {
            "Note": f"Food with name {new_food.name} created but record with the same name was found, consider "
                    f"updating it",
            "foods": new_food}
    elif query is None:
        add_and_commit(new_food, db)
        return {"foods": new_food}


