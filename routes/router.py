from typing import List
import uuid
from fastapi import APIRouter, Request, HTTPException, status
from bson.objectid import ObjectId

router = APIRouter()

@router.get("/ping")
async def ping(request: Request):
    return {"ping": "pong"}