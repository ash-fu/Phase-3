from flask import render_template, request
from phase3 import app
import pandas as pd
import numpy as np
from processPT import *

#server/pivot_table
@app.route("/pivot_table",methods=['POST', 'GET'])
def pivot_table():
	title = "Pivot Table"
	template_vars = {
		"title": title
	}

	filterCategory = request.form['Filter Category']
	filterMethod = request.form['Filter Method']
	filterValue = request.form['Filter Value']
	row = request.form['Row']
	column = request.form['Column']
	agg = request.form['agg']
	values = request.form['Values']
	
	filteredData = filterData(filterCategory,filterValue,filterMethod)
	table = constructPT(filteredData,row,column,values,agg)
	with open('templates/pivot_table.html' , 'w') as html:
		html.write('''
			{% extends "base.html" %}
			{% block content %}
			''')
		c = table.to_html()
		c = c.encode('ascii', 'ignore')
		html.write(c)


		html.write('''
			{% endblock %}
		''')
		# body = '''Filter Method: %s <br>
		# Filter Category: %s <br>
		# Filter Value: %s <br>
		# Aggregation: %s <br>

		# '''
		# body = body % (filterCategory,filterMethod,filterValue,agg)
		# html.write(body)

	return render_template("pivot_table.html",vars=template_vars)
