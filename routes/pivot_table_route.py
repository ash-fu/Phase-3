from flask import render_template
from phase3 import app
import pandas as pd
import numpy as np
from processPT import *

#server/pviot_table
@app.route("/pivot_table")
def pivot_table():
	filteredData = filterData(element,userInput,filterMethod)
	table = constructPT(data,rows,columns,values,agg)
	with open('templates/pivot_table.html' , 'w') as html:
		html.write('''
			{% extends "base.html" %}
			{% block content %}
			''')






		html.write('''
			{% endblock %}
		''')
	return render_template("pivot_table.html")
