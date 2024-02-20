from config import Config
from fastapi import FastAPI
from routes.router import router
from pymongo import MongoClient

config = Config()

app = FastAPI()

@app.on_event("startup")
def startup_db_client():
    app.mongodb_client = config.client
    app.database = config.db

app.include_router(router, prefix="/api")