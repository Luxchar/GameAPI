from fastapi import APIRouter, Request, HTTPException, status
from bson.objectid import ObjectId

putrouter = APIRouter()

@putrouter.put("/games/{game_id}", response_description="Update a single game")
async def update_game(game_id: str, request: Request):
    """ Update a single game """
    game_id = game_id.strip()
    updated_game_data = await request.json()
    updated_game = request.app.database.games.find_one_and_update(
        {"_id": ObjectId(game_id)},
        {"$set": updated_game_data},
        return_document=True
    )
    if updated_game:
        updated_game['_id'] = str(updated_game['_id'])
        return updated_game
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No game with that id")

