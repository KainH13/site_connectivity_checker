from flask_app import app

# import blueprints
from flask_app.blueprints.connectivity_check import connectivity_check
from flask_app.blueprints.user import user

# blueprints
app.register_blueprint(connectivity_check, url_prefix="/api/v1/connectivity_check")
app.register_blueprint(user, url_prefix="/api/v1/user")

if __name__ == "__main__":
    app.run(debug=True, port=4999)
