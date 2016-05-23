from flask import render_template, request
from phase3 import app
import pandas as pd
import numpy as np
from processPT import *


# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import csv

dataset = pd.read_csv("data_2012.csv")
dataset.head()
content = open("data_2012.csv")
reader = csv.reader(content)
header = reader.next();

#example print table = constructPT(data,"Date (Intervals)","Sex of Casualty","Number of Vehicles","sum")
#print table.to_html()


def filterData(element,userInput,filterMethod):
    if (filterMethod == ">"):
        filteredData =  dataset.loc[(dataset["%s"%(element)] > "%s"%(userInput)), header]
    elif (filterMethod == ">="):
        filteredData =  dataset.loc[(dataset["%s"%(element)] >= "%s"%(userInput)), header]
    elif (filterMethod == "<"):
        filteredData =  dataset.loc[(dataset["%s"%(element)] < "%s"%(userInput)), header]
    elif (filterMethod == "<="):
        filteredData =  dataset.loc[(dataset["%s"%(element)] <= "%s"%(userInput)), header]
    elif (filterMethod == "="):
        filteredData =  dataset.loc[(dataset["%s"%(element)] == "%s"%(userInput)), header]
    else:
        filteredData =  dataset.loc[(dataset["%s"%(element)] != "%s"%(userInput)), header]
    return filteredData
    

def constructPT(data,rows,columns,values,agg):
    
    if(agg == "sum"):
        agg_action = [np.sum]
    elif(agg == "minimum"):
        agg_action = [np.min]
    elif(agg == "maximum"):
        agg_action = [np.max]
    elif(agg == "median"):
        agg_action = [np.median]
    else:
        agg_action = [np.mean]

    table = pd.pivot_table(data,index=rows,columns=columns,values=values,\
    aggfunc=agg_action,fill_value=0,margins=True,dropna=True)
    table.columns = table.columns.droplevel(0)
    return table


#server/pivot_table
@app.route("/pivot_table", methods=['POST', 'GET'])
def pivot_table():
	title = "Pivot Table"
	template_vars = {
		"title": title
	}

	# filterCategory = request.form['Filter Category']
	# filterMethod = request.form['Filter Method']
	# filterValue = request.form['Filter Value']
	# row = request.form['Row']
	# column = request.form['Column']
	# agg = request.form['agg']
	# values = request.form['Values']


	row = request.form['row']
	col = request.form['col']
	values = request.form['data']
	filter_data = request.form['filter data']
	sign = request.form['sign']
	agg = request.form['agg']
	filter_value = request.form['filter_value']

	filteredData = filterData(filter_data, filter_value, sign)
	table = constructPT(filteredData, row, col, values, agg)

	#filteredData = filterData(filterCategory,filterValue,filterMethod)
	#table = constructPT(filteredData,row,column,values,agg)
	with open('templates/pivot_table.html' , 'w') as html:

		html.write('''
			{% extends "base.html" %}
			{% block content %}
			''')
			# +table.to_html())


		html.write('''
			{% endblock %}
		''')
		body = '''
		The row is: %s<br>
		The col is: %s<br>
		The data is: %s<br>
		The filter is: %s<br>
		The sign is: %s<br>
		The filter_value is: %s<br>

		'''

		body = body % (row, col, values, filter_data, sign, filter_value)

		body += table.to_html()
		# #body = body % (filterCategory,filterMethod,filterValue,agg)
		html.write(body)

		# html.write(table.to_html())
	return render_template("pivot_table.html",vars=template_vars)




