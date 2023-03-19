from userdataprocess.ActivityLevel import ActivityLevel
from userdataprocess.BMR import BMR
from userdataprocess.Calories import CaloriesIntake
from userdataprocess.MacroSplit import MacroSplit
from fastapi_sqlalchemy import db
# from sqlalchemy.orm import Session
import schemas
# from sqlalchemy.sql import func
import models
import time
from models import User as UserModel


def data(request):
    new_user = UserModel(
        name=request.name,
        age=request.age,
        height=request.height,
        weight=request.weight,
        activity_level=request.activity_level,
        diet_style=request.diet_style,
        body_type=request.body_type,
        gender=request.gender
    )
    return new_user


def data_processor(request):
    bmr_class = BMR(request.weight, request.height, request.age, request.gender)
    bmr = bmr_class.bmr
    activity_level_multiplier = ActivityLevel(request.activity_level).activity_level
    calories = CaloriesIntake(bmr, activity_level_multiplier, request.diet_style)
    macro_split = MacroSplit(calories.calories_daily, request.body_type)

    processed_data = models.ProcessedData(
        name=request.name,
        age=request.age,
        height=request.height,
        weight=request.weight,
        activity_level=request.activity_level,
        diet_style=request.diet_style,
        body_type=request.body_type,
        gender=request.gender,
        bmr=bmr,
        bmr7=bmr * 7,
        bmi=bmr_class.bmi,
        daily_calories=calories.calories_daily,
        weekly_calories=calories.calories_weekly,
        daily_protein=macro_split.protein,
        daily_carbs=macro_split.carbs,
        daily_fat=macro_split.fat,
    )
    print("ee: ", processed_data.__dict__)

    return processed_data


def update_user_basic_info(update_user, request: schemas.UserUpdate):
    update_user.age = request.age
    update_user.height = request.height
    update_user.weight = request.weight
    update_user.activity_level = request.activity_level
    update_user.diet_style = request.diet_style
    db.session.commit()


def update_user_processed_data(update_user):
    bmr_class = BMR(update_user.weight, update_user.height, update_user.age, update_user.gender)
    bmr = bmr_class.bmr
    activity_level_multiplier = ActivityLevel(update_user.activity_level).activity_level
    calories = CaloriesIntake(bmr, activity_level_multiplier, update_user.diet_style)
    macro_split = MacroSplit(calories.calories_daily, update_user.body_type)
    update_user.bmr = bmr
    update_user.bmr7 = bmr * 7
    update_user.bmi = bmr_class.bmi
    update_user.daily_calories = calories.calories_daily
    update_user.weekly_calories = calories.calories_weekly
    update_user.daily_protein = macro_split.protein
    update_user.daily_carbs = macro_split.carbs
    update_user.daily_fat = macro_split.fat
    # print(f"updData: "
    #       f"\nAge: {update_user.age}"
    #       f"\nHeight: {update_user.height}"
    #       f"\nWeight: {update_user.weight}"
    #       f"\nActivity: {update_user.activity_level}"
    #       f"\nDiet: {update_user.diet_style}"
    #       f"\nBody: {update_user.body_type}"
    #       f"\nGender: {update_user.gender}"
    #       f"\nBMI: {update_user.bmi}"
    #       f"\nBMR: {update_user.bmr}"
    #       f"\nBMR7: {update_user.bmr7}"
    #       f"\nDaily Calories: {update_user.daily_calories}"
    #       f"\nWeekly Calories: {update_user.weekly_calories}"
    #       )
    db.session.commit()


def update_user_age(user, request):
    user.age = request.age
    db.session.commit()


def update_everything(query, user_id, request):
    update_user_basic_info(query, request)
    db.session.commit()
    new_query = db.session.query(models.ProcessedData).filter(models.User.id == user_id).first()
    update_user_processed_data(new_query)


def update_user_height(user, request):
    user.height = request.height
    db.session.commit()


def update_user_weight(user, request):
    user.weight = request.weight
    db.session.commit()
