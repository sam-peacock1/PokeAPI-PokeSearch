# This is the main flask server
from dotenv import load_dotenv
from flask import Flask, render_template, request
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
    name = request.args.get('pokemon')
    print(name)
    return render_template('pokemon.html', name=name)

if __name__ == '__main__':
    app.run(host=host, port=port)