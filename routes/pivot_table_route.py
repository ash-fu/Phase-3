# coding=utf-8
from flask import render_template, request
from phase3 import app
import pandas as pd
import numpy as np
from processPT import *


# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import csv
import seaborn as sns
import matplotlib.pyplot as plt

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

	#table = pd.pivot_table(data,index=rows,columns=columns,values=values,\
	#aggfunc=agg_action,fill_value=0,margins=True,dropna=True)
	table = pd.pivot_table(data,index=rows,columns=columns,values=values,\
	aggfunc=agg_action,fill_value=0)
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
	filter_method = request.form['sign']
	agg = request.form['agg']
	filter_value = request.form['filter_value']

	filteredData = filterData(filter_data, filter_value, filter_method)

	

	# cm = sns.light_palette("green", as_cmap=True)

	# c = table.style.background_gradient(cmap=cm)
	# c.savefig("templates/table.png", dpi=50)

	# #filteredData = filterData(filterCategory,filterValue,filterMethod)
	# #table = constructPT(filteredData,row,column,values,agg)
	with open('templates/pivot_table.html' , 'w') as html:
		html.write('''
			{% extends "base.html" %}

			{% block customCSS %}
			<link rel="stylesheet" href="templates/css/pivot_table_builder.css" type="text/css">
 			<link rel="stylesheet" href="templates/stylesheets/dataset.css" type="text/css">
 			<link rel="stylesheet" href="templates/css/bootstrap-table.min.css" type="text/css">
 			<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap.min.css">            
 			{% endblock %}

 			{% block customJS %}
 			<!-- jQuery (necessary for Bootstrap's JavaScript plugins) -->
 			<!-- Latest compiled and minified JavaScript -->
 			<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/js/bootstrap.min.js"></script>
 			<!-- Latest compiled and minified JavaScript -->
 			<script src="https://cdnjs.cloudflare.com/ajax/libs/bootstrap-table/1.8.1/bootstrap-table.min.js"></script>
			{% endblock %}

			{% block content %}
			<p id = "table"></p>
			''')

		try:
			table = constructPT(filteredData, row, col, values, agg)
			# table = table.drop('All', axis=1)
	 	# 	table = table.drop('All')
	 		maxVal = table.values.max()
			c = table.to_html()
			c = c.encode('ascii', 'ignore')
			html.write(c)
		except:
			html.write('''<h1>Error</h1>
					<h2>INVALID INPUT!</h2>''')
		
		# c = table.to_html()
		# c = c.encode('ascii', 'ignore')
		# html.write(c)

		html.write('''
			{% endblock %}
		''')

	return render_template("pivot_table.html",vars=template_vars)


def webshow(img):
	savefig(img,dpi=50)
	print 'Content-Type: text/html\n'
	print '<img width="400" height="300" src="'+img+'" />'


# 	title = "Pivot Table"
# 	template_vars = {
# 		"title": title
# 	}
# 	row = request.form['row']
# 	col = request.form['col']
# 	values = request.form['data']
# 	filter_data = request.form['filter data']
# 	filter_method = request.form['sign']
# 	agg = request.form['agg']
# 	filter_value = request.form['filter_value']    
# 	filteredData = filterData(filter_data, filter_value, filter_method)
# 	table = constructPT(filteredData, row, col, values, agg)
	

# 	with open('templates/pivot_table.html' , 'w') as html:
# 		html.write('''
# 			{% extends "base.html" %}

# 			{% block customCSS %}
# 			<link rel="stylesheet" href="templates/stylesheets/dataset.css" type="text/css">
# 			<link rel="stylesheet" href="templates/css/bootstrap-table.min.css" type="text/css">
# 			<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap.min.css">            
# 			{% endblock %}

# 			{% block customJS %}
# 			<!-- jQuery (necessary for Bootstrap's JavaScript plugins) -->
# 			<script src="https://ajax.googleapis.com/ajax/libs/jquery/2.1.0/jquery.min.js"></script>
# 			<!-- Latest compiled and minified JavaScript -->
# 			<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/js/bootstrap.min.js"></script>
# 			<!-- Latest compiled and minified JavaScript -->
# 			<script src="https://cdnjs.cloudflare.com/ajax/libs/bootstrap-table/1.8.1/bootstrap-table.min.js"></script>
# 			{% endblock %}
# 			''')

# 		c = table.to_csv(column=False)

# 		html.write('''
# 			{% block content %}
# <table data-toggle = "table" data-pagination = "true">\r''')
		
# 		table = table.drop('All', axis=1)
# 		table = table.drop('All')
# 		maxVal = table.values.max()
# 		c = table.to_csv(column=False)
# 		r = 0
# 		for row in c:
# 			if r == 0:
# 				html.write('\t<thead>\r\t\t<tr>\r')
# 				for col in row:
# 					html.write('\t\t\t<th data-sortable="true">' + col + '</th>\r')
# 					html.write('\t\t</tr>\r\t</thead>\r')
# 					html.write('\t<tbody>\r')
# 			else:
# 				html.write('\t\t<tr>\r')
# 				for col in row:
# 					html.write('\t\t\t<td>' + col + '</td>\r')
# 					html.write('\t\t</tr>\r')
# 			r += 1
# 		html.write('\t</tbody>\r')
# 		html.write('</table>\r')

# 		html.write('''
# 			{% endblock %}
# 		''')

# 	return render_template("pivot_table.html",vars=template_vars)



	# filterCategory = request.form['Filter Category']
	# filterMethod = request.form['Filter Method']
	# filterValue = request.form['Filter Value']
	# row = request.form['Row']
	# column = request.form['Column']
	# agg = request.form['agg']
	# values = request.form['Values']
	# filteredData = filterData(filterCategory,filterValue,filterMethod)
	# table = constructPT(filteredData,row,column,values,agg)