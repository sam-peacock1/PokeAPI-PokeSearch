# This is the main flask server
from flask import Flask
from dotenv import load_dotenv
import os
# Load environment variables from .env file
load_dotenv()

# Get the host and port from environment variables
host = os.getenv('HOST')
port = os.getenv('PORT')

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello PokeAPI!'

if __name__ == '__main__':
    app.run(host=host, port=port)