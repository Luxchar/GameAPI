from fastapi import APIRouter, Body, Request, Response, HTTPException, status
from fastapi.encoders import jsonable_encoder
from typing import List
import uuid
from fastapi.encoders import jsonable_encoder
from bson import ObjectId

router = APIRouter()


@router.get("/games", response_description="List all games")
async def list_games(request: Request):
    """ List 10 games """
    pipeline = [
        {"$limit": 10},
        {"$project": {"_id": {"$toString": "$_id"}, "Title": 1, "Release Date": 1, "Developer": 1, "Publisher": 1, "Genres": 1, "Genres Splitted": 1, "User Score": 1, "User Ratings Count": 1, "Platforms Info": 1}}
    ]
    return list(request.app.database.games.aggregate(pipeline))


# ############################################## PSAHTEK MON CRUD ###################
# GET all games
@router.get("/games/all", response_description="List all games")
async def list_games(request: Request):
    """ List all games """
    pipeline = [
        
        {"$project": {"_id": {"$toString": "$_id"}, "Title": 1, "Release Date": 1, "Developer": 1, "Publisher": 1, "Genres": 1, "Genres Splitted": 1, "User Score": 1, "User Ratings Count": 1, "Platforms Info": 1}}
    ]
    return list(request.app.database.games.aggregate(pipeline))

# ############################################## GG mais que dans postman#######################
@router.post("/games", response_description="Add new game")
async def create_game(request: Request, game_data: dict):
    """ Add a new game """
    result = request.app.database.games.insert_one(game_data)
    return {"message": "jeu crée gg", "game_id": str(result.inserted_id)}
##############################################################################################################
@router.put("/games/{game_id}")
async def update_game(request: Request, game_id: str, game_data: dict):
    # boum le bon format
    update_data = jsonable_encoder(game_data)

    # Check exisance du jeu
    existing_game =  request.app.database.games.find_one({"_id": game_id})
    if existing_game:
        # maj
        await request.app.database.games.update_one({"_id": game_id}, {"$set": update_data})
        return {"message": "maj apliquée :)"}
    else:
        # ff
        raise HTTPException(status_code=404, detail="pas de jeu lol")



# DELETE a game
@router.delete("/games/{game_id}", response_description="Delete a game")
async def delete_game(request: Request, game_id: str):
    """ Delete a game """
    print(game_id)
    result =  request.app.database.games.delete_one({"_id": game_id})
    print(result)
    if result.deleted_count == 1:
        return {"message": "Game deleted successfully"}
    raise HTTPException(status_code=404, detail="Game not found")