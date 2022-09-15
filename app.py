from flask import Flask
from simple_pages import simple_pages
from flask_bootstrap import Bootstrap
def create_app():
    app = Flask(__name__)

    app.register_blueprint(simple_pages)

    return app




