from fastapi import APIRouter, Request, HTTPException, status
from bson.objectid import ObjectId
from typing import List

likesrouter = APIRouter()

@likesrouter.post("/like", response_description="add like", status_code=status.HTTP_201_CREATED)
async def like_game(request: Request):
    """ Like a game """
    body = await request.json()
    # check for token and game_id
    if not body.get("token") or not body.get("game_id"):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid request data")
    
    # check if token is valid
    if not request.app.database.users.find_one({"token": body["token"]}):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid user token")
    
    if request.app.database.games.find_one({"_id": ObjectId(body["game_id"])}):
        user = request.app.database.users.find_one({"token": body["token"]})
        if user:
            request.app.database.users.update_one({"token": body["token"]}, {"$push": {"likes": ObjectId(body["game_id"])}})
            return {
                "message": "Game liked successfully"
            }
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid user token")
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid game id")

@likesrouter.get("/liked", response_description="Get liked games", status_code=status.HTTP_200_OK)
async def get_liked_games(request: Request):
    """ Get liked games """
    body = await request.json()
    
    if not body.get("token"):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid request data")
    
    # check if token is valid
    if not request.app.database.users.find_one({"token": body["token"]}):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid user token")
    
    user = request.app.database.users.find_one({"token": body["token"]})
    if user:
        liked_games = request.app.database.users.find_one({"token": body["token"]})["likes"]
        # fetch game details
        liked_games = [request.app.database.games.find_one({"_id": game_id}) for game_id in liked_games]
        # convert ObjectId to string
        liked_games = [str(game_id) for game_id in liked_games]
        return {
            "liked_games": liked_games
        }
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid user token")

@likesrouter.get("/recommended", response_description="Get recommended games", status_code=status.HTTP_200_OK)
async def get_recommended_games(request: Request):
    """ Get recommended games """
    body = await request.json()
    
    if not body.get("token"):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid request data")
    
    # check if token is valid
    if not request.app.database.users.find_one({"token": body['token']}):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid user token")
    
    user = request.app.database.users.find_one({"token": body['token']})
    if user:
        liked_games = request.app.database.users.find_one({"token": body['token']})["likes"]
        recommended_games = []
        for game_id in liked_games:
            game = request.app.database.games.find_one({"_id": game_id})
            if game:
                recommended_games.extend(request.app.database.games.find({"$or": [{"Genres": game["Genres"]}, {"Publisher": game["Publisher"]}]}).limit(5))
            # convert ObjectId to string
            recommended_games = [str(game_id) for game_id in recommended_games]
        return {
            "recommended_games": recommended_games
        }
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid user token")