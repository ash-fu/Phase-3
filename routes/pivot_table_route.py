from flask import render_template
from phase3 import app
import pandas as pd
import numpy as np

#server/dataset
@app.route("/pivot_table")
def pivot_table(table):
	with open('templates/pivot_table.html' , 'w') as html:
		html.write('''
			<!DOCTYPE html>
			<html lang="en">
				<head>
				<meta charset="utf-8">
				<title>Pivot Table</title>
			''')
		table_ = table.to_html()
		html += table_
	return render_template("pivot_table.html")