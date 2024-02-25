from typing import List
import uuid
from fastapi import APIRouter, Request, HTTPException, status
from bson.objectid import ObjectId

router = APIRouter()

# @router.post("/games", response_description="rajoute ton jeu", response_model=Game)
# def create_game(game: Game, request: Request):
#     """ khalass 1 jeu dans poche """
#     new_game = game.dict()
#     result = request.app.database.games.insert_one(new_game)
#     if result.inserted_id:
#         return Game(**{**new_game, "Platforms Info": str(new_game.get("Platforms Info"))})
#     raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="on peut pas lajoute chef")

# @router.put("/games/{game_id}", response_description="Update ton jeu", response_model=Game)
# def update_game(game_id: str, game: Game, request: Request):
#     """ Update hehe """
#     existing_game = request.app.database.games.find_one({"id": game_id})
#     if existing_game:
#         updated_game = game.dict()
#         request.app.database.games.update_one({"id": game_id}, {"$set": updated_game})
#         return Game(**{**updated_game, "Platforms Info": str(updated_game.get("Platforms Info"))})
#     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="ton jeu existe ouuuuuuuuu")

# @router.delete("/games/{game_id}", response_description="jeu au goulag")
# def delete_game(game_id: str, request: Request):
#     """supprime jeu """
#     result = request.app.database.games.delete_one({"id": game_id})
#     if result.deleted_count == 1:
#         return {"message": "Game deleted successfully"}
#     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="ton jeu existe ? :o")