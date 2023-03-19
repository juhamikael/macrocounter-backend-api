from routers.foods_eaten import foods_eaten_functions as fe_funcs
from fastapi import APIRouter, HTTPException, status
from schemas import FoodEaten as FoodEaten_schema
from fastapi_sqlalchemy import db
from models import User, Food, FoodEaten, ProcessedData
from sqlalchemy.sql import func

router = APIRouter()


# ######################################################################################################################
# GET
# ######################################################################################################################
@router.get("/api/v1/users/{user_id}/foods_eaten", tags=["Get"], summary="Get food eaten by user")
def get_food_eaten_by_user(user_id: int):
    food_eaten = db.session.query(FoodEaten).filter(FoodEaten.user_id == user_id).all()
    user_daily_calories = db.session.query(ProcessedData.daily_calories).filter(User.id == user_id).first()
    sum_calories = db.session.query(func.sum(FoodEaten.calories).label("calories")).filter(
        FoodEaten.user_id == user_id).first()
    sum_fat = db.session.query(func.sum(FoodEaten.fat).label("fat")).filter(
        FoodEaten.user_id == user_id).first()
    sum_carbs = db.session.query(func.sum(FoodEaten.carbs).label("carbs")).filter(
        FoodEaten.user_id == user_id).first()
    sum_protein = db.session.query(func.sum(FoodEaten.protein).label("protein")).filter(
        FoodEaten.user_id == user_id).first()
    return {"food_eaten": food_eaten,
            "sum_calories": sum_calories[0],
            "sum_fat": sum_fat[0],
            "sum_carbs": sum_carbs[0],
            "sum_protein": sum_protein[0],
            "daily_calories": user_daily_calories[0]
    }

# ######################################################################################################################
# POST
# ######################################################################################################################
@router.post("/api/v1/foods/eaten/{user_id}", tags=["Post"], summary="Create food eaten by user")
def create_food_eaten_by_user(user_id: int, request: FoodEaten_schema):
    food = db.session.query(Food).filter(Food.id == request.food_id).first()
    user = db.session.query(User).filter(User.id == user_id).first()
    if not food:
        raise HTTPException(status_code=404, detail="Food not found")
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return fe_funcs.food_eaten_by_user(user_id, request, food, db.session)


# ######################################################################################################################
# DELETE
# ######################################################################################################################
@router.delete("/api/v1/foods/user/eatenfoods", tags=["Delete"], summary="Delete food eaten by user")
def delete_food_eaten_by_user(food_eaten_id: int):
    check_if_exist = db.session.query(FoodEaten).filter(FoodEaten.id == food_eaten_id).first()
    if not check_if_exist:
        raise HTTPException(status_code=404, detail=f"Food eaten with ID {food_eaten_id} not found")
    db.session.query(FoodEaten).filter(FoodEaten.id == food_eaten_id).delete(synchronize_session=False)
    db.session.commit()
    return f"Food eaten {food_eaten_id} deleted"


@router.delete("/api/v1/users/{user_id}/eaten", tags=["Delete"], summary="Delete all eaten foods by user")
def delete_all_eaten_foods_by_user(user_id: int):
    check_if_exists = db.session.query(FoodEaten).filter(FoodEaten.user_id == user_id).first()
    if not check_if_exists:
        raise HTTPException(status_code=404, detail=f"User with ID {user_id} not found")
    db.session.query(FoodEaten).filter(FoodEaten.user_id == user_id).delete(synchronize_session=False)
    db.session.commit()
    return f"All eaten foods by user {user_id} deleted"
