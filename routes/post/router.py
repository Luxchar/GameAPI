from fastapi import APIRouter, Request, HTTPException, status
from bson.objectid import ObjectId

postrouter = APIRouter()

@postrouter.post("/games", response_description="ajoute jeu", status_code=status.HTTP_201_CREATED)
async def add_game(request: Request, game_data: dict):
    """ ajout jeu """
    # requete tu connais
    inserted_game = request.app.database.games.insert_one(game_data)
    
    # on verif si cest good
    if inserted_game.inserted_id:
        # rep cest ok (201)
        return {
            "message": "C'est dans la boite",
            "inserted_game_id": str(inserted_game.inserted_id)
        }
    
    
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="echec critique")

@postrouter.post("/games/multiple", response_description="aj dé games", status_code=status.HTTP_201_CREATED)
async def add_x_games(request: Request, games_data: list):
    """ games games"""
    # list verif
    inserted_games_ids = []
    
    # on  parcourt list de jeu
    for game_data in games_data:
        
        inserted_game = request.app.database.games.insert_one(game_data)
        
        
        if inserted_game.inserted_id:
           
            inserted_games_ids.append(str(inserted_game.inserted_id))
        else:
            # echec
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"echec sur: {game_data}")
    
    # renvoie les ids des jeux crése
    return {
        "message": "ça va game fort",
        "inserted_games_ids": inserted_games_ids
    }