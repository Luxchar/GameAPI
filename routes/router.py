from fastapi import APIRouter, Body, Request, Response, HTTPException, status
from fastapi.encoders import jsonable_encoder
from typing import List
import uuid

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
# @router.get("/games", response_description="List all games", response_model=List[Game])
# def list_games(request: Request):
#     """ List all games """
#    #problème de type de platforms info > besoin de conversion en str 
#     # Création dico en combinant le dico game  + nouvelle paire clé-valeur  "Platforms Info" converti str
#     games = [
#         Game(**{**game, "Platforms Info": str(game.get("Platforms Info"))}) 
#         for game in request.app.database.games.find()
#     ]
#     return games



# @router.get("/publishers", response_description="Liste des éditeurs", response_model=List[str])
# def list_publishers(request: Request):
#     """ Liste tous les éditeurs """
#     publishers = request.app.database.games.distinct("Publisher")
#     return publishers

# ############################################### AUUUEEEEEEE#############

# @router.get(
#     "/games/{id}",
#     response_description="Get a single game",
#     response_model=Game,
# )
# def get_game(id:str,request: Request):
#     """
#     chope le jeu par id.
#     """
#     # utilisation id
#     ob_id = id.strip()
    
#     game =  request.app.database.games.find_one({"id": ob_id})
#     if game:
#         # conversion tu connais
#         game["Platforms Info"] = str(game.get("Platforms Info"))
#         return game
#     else:
#         # erreur si fail
#         raise HTTPException(status_code=404, detail=f"Game {id} pas found")


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