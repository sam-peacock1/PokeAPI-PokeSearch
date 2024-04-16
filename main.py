# This is the main flask server
from dotenv import load_dotenv
from flask import Flask, render_template, request, send_from_directory
import os
# Load environment variables from .env file
load_dotenv()

# Get the host and port from environment variables
host = os.getenv('HOST')
port = os.getenv('PORT')

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/pokemon')
def get_pokemon():
    # When we search for a pokemon we store the name of the pokemon in the url as a parameter (the bit after the ? in the url)
    name = request.args.get('pokemon')
    if name is None:
        return render_template('index.html')
    
    name = name.title()
    return render_template('pokemon.html', name=name)

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')

if __name__ == '__main__':
    app.run(host=host, port=port, debug=True)