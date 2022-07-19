from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
import os

# import blueprints
from flask_app.controllers.connectivity_check import connectivity_check

load_dotenv()

# initialize app
app = Flask(__name__)
CORS(app)
app.secret_key = os.getenv("SECRET_KEY")

# blueprints
app.register_blueprint(connectivity_check, url_prefix="/api/v1/connectivity_check")
