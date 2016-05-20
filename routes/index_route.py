from flask import Flask, render_template, request
from phase3 import app
import csv
import pandas as pd
import numpy as np
import jinja2
import readdata

#server/
@app.route("/")
def index():
	title = "Traffic Accident Statistics"
	template_vars = {
		"title": title
	}
	return render_template("index.html",vars=template_vars)