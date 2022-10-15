from flask import Blueprint, render_template,abort, request
from jinja2 import TemplateNotFound
import pytube

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

@simple_pages.route('/calculator')
def calc():
    try:
        return render_template('calc.html')
    except TemplateNotFound:
        abort(404)

@simple_pages.route('/youtube', methods =["GET", "POST"])
def ytDownloader():
    if request.method =="POST":
        link = str(request.form.get("link"))
        yt=pytube.YouTube(link)
        stream = yt.streams.get_audio_only()
        stream.download()

    try:
        return render_template('yt_down.html')
    except TemplateNotFound:
        abort(404)
