from flask_app import app
from flask_app.controllers import connectivity_check

if __name__ == "__main__":
    app.run(debug=True, port=4999)
