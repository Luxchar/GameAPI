from fastapi import APIRouter, Request, HTTPException, status
from bson.objectid import ObjectId

deleterouter = APIRouter()

@deleterouter.delete("/games/{game_id}", response_description="Delete a single game")
async def delete_game(game_id: str, request: Request):
    """ Delete un jeeu """
    game_id = game_id.strip()
    deleted_game = request.app.database.games.find_one_and_delete({"_id": ObjectId(game_id)})
    if deleted_game:
        deleted_game['_id'] = str(deleted_game['_id'])
        return deleted_game
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="jeu no existant")


