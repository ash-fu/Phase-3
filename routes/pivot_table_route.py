from flask import render_template
from phase3 import app
import pandas as pd
import numpy as np

#server/dataset
@app.route("/pivot_table")
def pivot_table(table):
	title = "Pivot Table"
	template_vars = {
		"title": title
	}
	with open('templates/pivot_table.html' , 'w') as html:
		html.write('''
		{% extends "base.html" %}
		
		''')
		table_ = table.to_html()
		html += table_
	return render_template("pivot_table.html", vars=template_vars)