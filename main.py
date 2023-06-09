from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from fastapi_sqlalchemy import DBSessionMiddleware
from starlette.middleware.cors import CORSMiddleware
from routers.users import user
from routers.foods import food
from routers.foods_eaten import food_eaten
import os
from dotenv import load_dotenv
load_dotenv()

app = FastAPI()
DATABASE_URL = os.getenv('DATABASE_URL')

app.add_middleware(CORSMiddleware,
                   allow_origins=[
                       "https://projects.macrocounter.juhamikael.info",
                       "https://macrocounter-frontend.vercel.app*",
                       "https://projects.macrocounter.juhamikael.me",
                       "https://macrocounter.juhamikael.me*",
                       "http://*.macrocounter.juhamikael.me/*",
                       "https://macrocounter.juhamikael.me",
                       "http://localhost:3000",
                       "http://localhost:8080",
                       "http://localhost:5050",
                       "http://localhost:8000"],
                   allow_credentials=True,
                   allow_methods=["*"],
                   allow_headers=["*"], )

app.add_middleware(
    DBSessionMiddleware,
    db_url=os.environ.get('DATABASE_URL'))

app.include_router(user.router)
app.include_router(food.router)
app.include_router(food_eaten.router)


@app.get("/", tags=["ROOT"], summary="Root redirect")
async def docs_redirect():
    return RedirectResponse(url='/docs')
