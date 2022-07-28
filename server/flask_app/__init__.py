from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
import os

# load environmental variables
load_dotenv()

# initialize app
app = Flask(__name__)
CORS(app)  # allows front end react app to access endpoints
app.secret_key = os.getenv("SECRET_KEY")
