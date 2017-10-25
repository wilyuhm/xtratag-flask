from flask import Flask
from flask import render_template
from flask import request

from micawber.providers import bootstrap_basic
from micawber.contrib.mcflask import add_oembed_filters

from insta_api import run_xtratag


app = Flask(__name__)

oembed_providers = bootstrap_basic()
add_oembed_filters(app, oembed_providers)

@app.route('/')
def example_view():
    text = request.args.get('text', 'http://www.youtube.com/watch?v=nda_OSWeyn8')
    html = request.args.get('html', """
<p>This is a test</p>
<p>http://www.youtube.com/watch?v=nda_OSWeyn8</p>
<p>This will get rendered as a link: http://www.youtube.com/watch?v=nda_OSWeyn8</p>
<p>This will not be modified: <a href="http://www.google.com/">http://www.youtube.com/watch?v=nda_OSWeyn8</a></p>
    """)
    return render_template('hello.html', text=text, html=html)

# url_for('static', filename='style.css')

@app.route('/xtratag')
def run():
	oembed_codes = run_xtratag('jumpingstilts')
	return render_template('xtratag.html', oembed_codes=oembed_codes)
