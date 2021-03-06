from flask import Flask
from flask import render_template

from micawber.providers import bootstrap_basic
from micawber.contrib.mcflask import add_oembed_filters

from insta_api import run_xtratag


app = Flask(__name__)

oembed_providers = bootstrap_basic()
add_oembed_filters(app, oembed_providers)

@app.route('/')
def hello(name=None):
    return render_template('hello.html', name=name)

# url_for('static', filename='style.css')

@app.route('/xtratag')
def run():
	media_files = run_xtratag('sdzoo')
	return render_template('xtratag.html', media_files=media_files)
