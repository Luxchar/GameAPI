import requests
from config import Config

config = Config()

# Base URL of your API
base_url = "http://127.0.0.1:5000/api"

# Function to obtain all games
def get_all_games():
    response = requests.get(f"{base_url}/games/all")
    if response.status_code == 200:
        return response.json()
    else:
        print("Erreur lors de la récupération des jeux:", response.text)
        return None

# Function to create a game
def create_game(game_data):
    response = requests.post(f"{base_url}/games", json=game_data)
    if response.status_code == 200:
        return response.json()
    else:
        print("Erreur lors de la création du jeu:", response.text)
        return None

# Function to update a game
def update_game(game_id, game_data):
    response = requests.put(f"{base_url}/games/{game_id}", json=game_data)
    if response.status_code == 200:
        return response.json()
    else:
        print("Erreur lors de la mise à jour du jeu:", response.text)
        return None

# Function to delete a game
def delete_game(game_id):
    response = requests.delete(f"{base_url}/games/{game_id}")
    if response.status_code == 200:
        return response.json()
    else:
        print("Erreur lors de la suppression du jeu:", response.text)
        return None

# Examples of usage
if __name__ == "__main__":
    # Obtain all games
    print("Liste de tous les jeux:")
    print(get_all_games())

    # Create a new game
    new_game_data = {
        "Title": "Nouveau jeu",
        "Release Date": "2024-02-25",
        "Developer": "Nouveau développeur",
        "Publisher": "Nouveau éditeur",
        "Genres": "Nouveau genre",
        "Genres Splitted": ["Nouveau genre"],
        "User Score": 9.0,
        "User Ratings Count": 100,
        "Platforms Info": [{"Platform": "Nouvelle plateforme"}]
    }
    print("Nouveau jeu créé:")
    print(create_game(new_game_data))

    # Update an existing game
    game_id_to_update = "65da0d6f8887f2cd78ba3fd8"
    updated_game_data = {
        "Title": "Jeu mis à jour",
        "Developer": "Développeur mis à jour"
    }
    print("Jeu mis à jour:")
    print(update_game(game_id_to_update, updated_game_data))

    # Delete a game
    game_id_to_delete = "65da0d6f8887f2cd78ba3fd8"
    print("Jeu supprimé:")
    print(delete_game(game_id_to_delete))
