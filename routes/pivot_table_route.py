from flask import render_template
from phase3 import app
import pandas as pd
import numpy as np

#server/dataset
@app.route("/pivot_table")
<<<<<<< HEAD
def pivot_table():
	with open('templates/pivot_table.html' , 'w') as html:
		html.write('''
			<!DOCTYPE html>
			<html lang="en">
				<head>
				<meta charset="utf-8">
				<title>Pivot Table</title>

				</head>
				<body>
				<div id="row"><p>The row is: </p></div>
				<script>
					function show() {
    					document.getElementById("row").innerHTML = window.location.serach;
					}
				</script>
				</body>

			</html>
			''')
		#table_ = table.to_html()
		#html += table_
	return render_template("pivot_table.html")
=======
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
>>>>>>> 6254edd4afc9687148978a31169b4bbf6c8fd577
