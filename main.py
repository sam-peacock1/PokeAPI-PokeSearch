# This is the main flask server
from dotenv import load_dotenv
from flask import Flask, render_template, request, send_from_directory
import os
from poke_api import *

# Load environment variables from .env file
load_dotenv()

# Get the host and port from environment variables
host = os.getenv('HOST')
port = os.getenv('PORT')

if host == None:
    host = '127.0.0.1'
if port == None:
    port = '5000'

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/pokemon')
def get_pokemon():
    # When we search for a pokemon we store the name of the pokemon in the url as a parameter (the bit after the ? in the url)
    name = request.args.get('pokemon')
    pokemon_info = get_pokemon_info(name)

    if name is None: # Return the user back to the main page if they didn't enter anything
        return render_template('index.html')
    
    if pokemon_info is None: # The API didn't have a pokemon by the name we were looking for
        return render_template('not_found.html', name=name)

    pokemon_name = pokemon_info['name'].title()
    pokemon_height = pokemon_info['height']/10
    pokemon_weight = pokemon_info['weight']/10
    pokemon_abilities = ', '.join(pokemon_info['abilities'])
    pokemon_types = ', '.join(pokemon_info['types'])
    return render_template('pokemon.html', 
                           name= pokemon_name,
                           type= pokemon_types,
                           height = pokemon_height,
                           weight = pokemon_weight,
                           abilities = pokemon_abilities
                           )

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')

if __name__ == '__main__':
    print(f"PokeSearch running on {host}:{port}")
    app.run(host=host, port=port, debug=True)

