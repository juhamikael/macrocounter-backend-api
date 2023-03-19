from fastapi import APIRouter, HTTPException, status
from fastapi_sqlalchemy import db
# from backend.app.routers.users import user_functions as user_f
from routers.foods import food_functions as food_f
from schemas import FoodIn as FoodIn_schema, FoodNameUpdate as FoodNameUpdate_schema, \
    FoodUpdate as FoodUpdate_schema
from models import Food

router = APIRouter()


# ######################################################################################################################
# GET
# ######################################################################################################################
@router.get("/api/v1/foods", tags=["Get"], summary="all foods", description="Returns the info food sent")
def get_all_foods():
    foods = db.session.query(Food).all()
    return {"foods": foods}


@router.get("/api/v1/foods/{food_id}", tags=["Get"], summary="Get food by id")
def get_food_by_id(food_id: int):
    new_food = db.session.query(Food).filter(Food.id == food_id).first()
    if not new_food:
        raise HTTPException(status_code=404, detail="Food not found")
    return {"food": new_food}


# ######################################################################################################################
# POST
# ######################################################################################################################
@router.post("/api/v1/foods", tags=["Post"], summary="Create food")
async def create_food(new_food: FoodIn_schema):
    post_food = food_f.post_food(new_food, db.session)
    return post_food


# ######################################################################################################################
# PUT
# ######################################################################################################################
@router.put("/api/foods/{food_id}", tags=["Update"], status_code=status.HTTP_202_ACCEPTED)
def update_food_macros(food_id: int, request: FoodUpdate_schema):
    food = db.session.query(Food).filter(Food.id == food_id).first()
    if not food:
        raise HTTPException(status_code=404, detail="Food not found")
    food_f.update_macros(food, request, db.session)
    return f"Food {food_id} info updated"


# Update food name
@router.put("/api/foods/{food_id}/names", tags=["Update"], status_code=status.HTTP_202_ACCEPTED)
def update_food_name(food_id: int, request: FoodNameUpdate_schema):
    food = db.session.query(Food).filter(Food.id == food_id).first()
    if not food:
        raise HTTPException(status_code=404, detail="Food not found")
    query_name = db.session.query(Food).filter(Food.name == request.name).first()
    food_f.update_name(food, request, db.session)
    if query_name:
        return {
            "Note": f"Food with name {request.name} updated but record with the same name was found, consider "
                    f"using different name",
            "Message": f"Food {food_id} info updated"}
    else:
        return {"Message": f"Food {food_id} info updated"}


# Foods Delete
@router.delete("/api/foods/{food_id}", tags=["Delete"], summary="Delete food by id")
def delete_food(food_id: int):
    if not db.session.query(Food).filter(Food.id == food_id).first():
        raise HTTPException(status_code=404, detail=f"Food with id {food_id} not found")
    db.session.query(Food).filter(Food.id ==
                                  food_id).delete(synchronize_session=False)
    db.session.commit()
    return f"Food {food_id} deleted"
