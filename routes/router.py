from typing import List
import uuid
from fastapi import APIRouter, Request, HTTPException, status
from bson.objectid import ObjectId

router = APIRouter()

@router.get("/ping")
async def ping(request: Request):
    """ Check if the API is running """
    return {"ping": "pong"}

# like a game

# get games liked

# get recommended games based on likes(games that have the same genre, publisher, etc)