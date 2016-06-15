from flask import render_template
from phase3 import app

#Front page of our website. Serves as the index, 
#containing links to the other routes/pages

#server/
@app.route("/")
def index():
	return render_template("index.html")