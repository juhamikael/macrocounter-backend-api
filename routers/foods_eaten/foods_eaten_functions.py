from models import Food, FoodEaten, User, ProcessedData
import time


# def update_user_calories_left(user_id, db):
#     user = db.session.query(ProcessedData).filter(User.id == user_id).first()
#     calories_consumed = db.query(func.sum(FoodEaten.calories).label("calories")).filter(
#         FoodEaten.user_id == user_id).first()["calories"]
#     user.calories_left_today = user.daily_calories - calories_consumed
#     user.calories_consumed = calories_consumed
#     db.commit()

def food_eaten_by_user(user_id, request, new_food_eaten, db):
    quantity = request.quantity / 100
    foods = db.query(Food).filter(Food.id == request.food_id).first()
    new_food = FoodEaten(
        user_id=user_id,
        food_id=request.food_id,
        food_name=foods.name,
        quantity=request.quantity,
        # meal_type=request.meal_type,
        protein=new_food_eaten.protein * quantity,
        carbs=new_food_eaten.carbs * quantity,
        fat=new_food_eaten.fat * quantity,
        calories=int((new_food_eaten.carbs * 4 +
                      new_food_eaten.fat * 9 +
                      new_food_eaten.protein * 4) * quantity),
        time=time.strftime("%H:%M:%S", time.localtime())
    )
    print("\n\n\n Food", new_food_eaten.__dict__, "\n\n\n")
    print(f"user_id: {user_id}")
    print(f"quantity: {quantity}")
    print(f"foods_query: {foods.__dict__}")
    print(f"new_food: {new_food.__dict__}")
    db.add(new_food)
    db.commit()
    db.refresh(new_food)
    return {"food_eaten": new_food}
