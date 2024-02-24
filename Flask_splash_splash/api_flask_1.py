from flask import Flask, jsonify, request

from pymongo import MongoClient
from bson.json_util import dumps
from flask_pymongo import PyMongo
import os
from dotenv import load_dotenv


load_dotenv()
routeurs = Flask(__name__)  # Pour initialiser l'application
routeurs.config["DEBUG"] = True # Pour activer le débogage et le rechargement automatique du code

routeurs.config['MONGO_DBNAME'] = os.getenv("DATABASE_NAME")
routeurs.config['MONGO_URI'] = os.getenv("MONGO_URL")
mongo = PyMongo(routeurs)
collection = mongo.db.games

# All jeu
@routeurs.route('/api/games/all', methods=['GET'])
def list_games():
    pipeline = [
        {"$project": {"_id": {"$toString": "$_id"}, "Title": 1, "Release Date": 1, "Developer": 1, "Publisher": 1, "Genres": 1, "Genres Splitted": 1, "User Score": 1, "User Ratings Count": 1, "Platforms Info": 1}}
    ]
    games = list(mongo.games.aggregate(pipeline))
    return dumps(games)

# créer
@routeurs.route('/api/games', methods=['POST'])
def create_game():
    game_data = request.json
    result = mongo.games.insert_one(game_data)
    return jsonify({"message": "jeu créé", "game_id": str(result.inserted_id)})
# maj jeu
@routeurs.route('/api/games/<game_id>', methods=['PUT'])
def update_game(game_id):
    game_data = request.json 
    # Update the game in the database
    result = mongo.games.update_one({"_id": game_id}, {"$set": game_data})
    
    # Check if the game was found and updated
    if result.matched_count == 1 and result.modified_count == 1:
        return jsonify({"message": "Game updated successfully"})
    else:
        return jsonify({"error": "Game not found or could not be updated"})
# supress game
@routeurs.route('/api/games/<game_id>', methods=['DELETE'])
def delete_game(game_id):
    result = mongo.games.delete_one({"_id": game_id})
    if result.deleted_count == 1:
        return jsonify({"message": "Jeu supprimé hehe"})
    else:
        return jsonify({"error": "Jeu ."})


if __name__ == '__main__':
   routeurs.run(debug=True)
