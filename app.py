from flask import Flask, render_template
from simple_pages import simple_pages
from flask_bootstrap import Bootstrap

def page_not_found(e):
    return render_template("404.html"), 404
app = Flask(__name__)

app.register_blueprint(simple_pages)
app.register_error_handler(404, page_not_found)

if __name__ == '__main__':
    app.run()

