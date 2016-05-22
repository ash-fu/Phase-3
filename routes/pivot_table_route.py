from flask import render_template
from phase3 import app
import pandas as pd
import numpy as np

#server/pviot_table
@app.route("/pivot_table")
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
	return render_template("pivot_table.html")
