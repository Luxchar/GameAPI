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

@putrouter.put("/games/multiple", response_description="Update multiple games")
async def update_multiple_games(request: Request):
    """ Update multiple games """
    updated_games_data = await request.json()
    updated_games_ids = []
    for updated_game_data in updated_games_data:
        game_id = updated_game_data.get('_id')
        if game_id:
            game_id = game_id.strip()
            updated_game = request.app.database.games.find_one_and_update(
                {"_id": ObjectId(game_id)},
                {"$set": updated_game_data},
                return_document=True
            )
            if updated_game:
                updated_game['_id'] = str(updated_game['_id'])
                updated_games_ids.append(str(game_id))
            else:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"No game with id {game_id}")
        else:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="'_id' field is required for each game")
    return {
        "message": "Games updated successfully",
        "updated_games_ids": updated_games_ids
    }