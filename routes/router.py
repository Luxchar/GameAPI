from fastapi import APIRouter, Body, Request, Response, HTTPException, status
from fastapi.encoders import jsonable_encoder
from typing import List

from models.game import Game

router = APIRouter()

@router.get("/games", response_description="List all games", response_model=List[Game])
def list_games(request: Request):
    """ List 10 games """
    games = request.app.database.games.find().limit(10)
    return games