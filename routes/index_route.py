from flask import render_template
from phase3 import app

#server/
@app.route("/")
def index():
	return render_template("index.html")