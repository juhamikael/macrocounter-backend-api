from routers.users import user_functions as user_f
from fastapi import APIRouter, HTTPException, status
from fastapi_sqlalchemy import db
from schemas import UserIn as SchemaUser
from schemas import \
    UserUpdate as SchemaUserUpdate, \
    UpdateAge as SchemaUpdateAge, \
    UpdateHeight as SchemaUpdateHeight, \
    UpdateWeight as SchemaUpdateWeight
from models import ProcessedData, User

router = APIRouter()


def get_update_schema(query):
    return SchemaUserUpdate(height=query.height, weight=query.weight,
                            age=query.age, activity_level=query.activity_level, diet_style=query.diet_style)


def select_user_where_id(user_id: int):
    query = db.session.query(User).filter(User.id == user_id).first()
    if not query:
        raise HTTPException(status_code=404, detail="User not found")
    return query


# ######################################################################################################################
# GET
# ######################################################################################################################
@router.get("/api/v1/users", tags=["Get"], summary="All users base data", description="Returns the info users sent")
async def get_all_users():
    users = db.session.query(User).all()
    return {"users": users}


@router.get("/api/v1/users_processed_data", tags=["Get"], summary="All users processed data")
async def get_all_users():
    users = db.session.query(ProcessedData).all()
    return {"users": users}


@router.get("/api/v1/users/{user_id}", tags=["Get"], summary="Get user base data by id ")
def get_user_base_info(user_id: int):
    user = db.session.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return {"user": user}


@router.get("/api/v1/users/processed_data/{user_id}", tags=["Get"], summary="Get user processed data by id ")
def get_user_processed_data_by_id(user_id: int):
    user = db.session.query(ProcessedData).filter(User.id == user_id).first()
    return {"user": user}


# ######################################################################################################################
# POST
# ######################################################################################################################
@router.post("/api/v1/users", tags=["Post"], summary="Create users", response_model=SchemaUser)
async def create_user(new_user: SchemaUser):
    db_user = user_f.data(new_user)
    processor = user_f.data_processor(db_user)
    db.session.add(processor)
    db.session.commit()
    return processor


######################################################################################################################
# PUT
######################################################################################################################
@router.put("/api/v1/users/{user_id}", tags=["Update"], status_code=status.HTTP_202_ACCEPTED)
def update_user(user_id: int, request: SchemaUserUpdate):
    query = select_user_where_id(user_id)
    user_f.update_user_basic_info(query, request)
    new_query = db.session.query(ProcessedData).filter(User.id == user_id).first()
    user_f.update_user_processed_data(new_query)
    return f"User {user_id} info updated"


@router.put("/api/v1/users/update_age/{user_id}", tags=["Update"], status_code=status.HTTP_202_ACCEPTED)
def update_user_age(user_id: int, request: SchemaUpdateAge):
    query = select_user_where_id(user_id)
    user_f.update_user_age(query, request)
    update_schema = get_update_schema(query)
    new_query = db.session.query(User).filter(User.id == user_id).first()
    user_f.update_everything(new_query, user_id, update_schema)
    return f"User {user_id} age updated"


@router.put("/api/v1/users/update_height/{user_id}", tags=["Update"], status_code=status.HTTP_202_ACCEPTED)
def update_user_height(user_id: int, request: SchemaUpdateHeight):
    query = select_user_where_id(user_id)
    user_f.update_user_height(query, request)
    update_schema = get_update_schema(query)
    new_query = db.session.query(User).filter(User.id == user_id).first()
    user_f.update_everything(new_query, user_id, update_schema)
    return f"User {user_id} height updated"


@router.put("/api/v1/users/update_weight/{user_id}", tags=["Update"], status_code=status.HTTP_202_ACCEPTED)
def update_user_weight(user_id: int, request: SchemaUpdateWeight):
    query = select_user_where_id(user_id)
    user_f.update_user_weight(query, request)
    update_schema = get_update_schema(query)
    new_query = db.session.query(User).filter(User.id == user_id).first()
    user_f.update_everything(new_query, user_id, update_schema)
    return f"User {user_id} weight updated"


######################################################################################################################
# DELETE
######################################################################################################################
@router.delete("/api/v1/users/{user_id}", tags=["Delete"], summary="Delete user by id")
def delete_user(user_id: int):
    check_if_exist = select_user_where_id(user_id)
    db.session.query(User).filter(User.id == user_id).delete(synchronize_session=False)
    db.session.commit()
    return f"User {user_id} deleted"
