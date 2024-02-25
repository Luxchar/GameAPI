from config import Config
from fastapi import FastAPI
from pymongo import MongoClient

from routes.router import router
from routes.get.router import getrouter
from routes.post.router import postrouter
from routes.put.router import putrouter
from routes.delete.router import deleterouter

config = Config()

app = FastAPI()

@app.on_event("startup")
def startup_db_client():
    app.mongodb_client = config.client
    app.database = config.db

app.include_router(router, prefix="/api")
app.include_router(getrouter, prefix="/api/get")
app.include_router(postrouter, prefix="/api/post")
app.include_router(putrouter, prefix="/api/put")
app.include_router(deleterouter, prefix="/api/delete")
