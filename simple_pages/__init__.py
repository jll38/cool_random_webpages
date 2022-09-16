from flask import Blueprint, render_template,abort
from jinja2 import TemplateNotFound

simple_pages = Blueprint('simple_pages', __name__,
                         template_folder='templates')
@simple_pages.route('/')
def home():
    try:
        return render_template('index.html')
    except TemplateNotFound:
        abort(404)

@simple_pages.route('/NumGenerator')
def randNum():
    try:
        return render_template('rand.html')
    except TemplateNotFound:
        abort(404)

@simple_pages.route('/piglatin')
def pigLatin():
    try:
        return render_template('piglatin.html')
    except TemplateNotFound:
        abort(404)