from flask import Flask
from simple_pages import simple_pages
from flask_bootstrap import Bootstrap

app = Flask(__name__)

app.register_blueprint(simple_pages)

if __name__ == '__main__':
    app.run()

