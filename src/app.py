from flask import Flask
from model import db
import time
from blueprints.store_blueprint import store_api

def create_app():
    app = Flask(__name__)
    app.register_blueprint(store_api)
    return app


if __name__ == "__main__":
    app = create_app()
    app.run()