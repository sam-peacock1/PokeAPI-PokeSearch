#import pokepy
import json
import requests



#class pokemon:
#    def __init__(self):
#        self.client = pokepy.V2Client()

def get_pokemon_info(pokemon_name):
        url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}"
        response = requests.get(url)
    
        if response.status_code == 200:
            pokemon_data = response.json()
            pokemon_info = {
                "name": pokemon_data["name"],
                "types": [type_data["type"]["name"] for type_data in pokemon_data["types"]],
                "height": pokemon_data["height"],
                "weight": pokemon_data["weight"],
                "abilities": [ability["ability"]["name"] for ability in pokemon_data["abilities"]],
        }
            return pokemon_info
        else:
            return None

#Bellow is just a test
#pokemon_name = input("Enter the Pokémon name: ")
#pokemon_info = get_pokemon_info(pokemon_name)
#
#if pokemon_info:
#    print(f"Name: {pokemon_info['name']}")
#    print(f"Height: {pokemon_info['height']}")
#    print(f"Weight: {pokemon_info['weight']}")
#    print(f"Abilities: {', '.join(pokemon_info['abilities'])}")
#    print(f"Types: {', '.join(pokemon_info['types'])}")
#else:
#    print("Pokémon not found!")
