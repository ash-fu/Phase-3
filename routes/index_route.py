from flask import render_template
from phase3 import app

#server/
@app.route("/")
def index():
	title = "Traffic Accident Statistics"
	template_vars = {
		"title": title
	}
	return render_template("index.html",vars=template_vars)