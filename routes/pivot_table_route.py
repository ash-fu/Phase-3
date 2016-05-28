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


# Filter data 
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
    

# Build pivot table
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
	aggfunc=agg_action)
	table.columns = table.columns.droplevel(0)
	return table


#server/pivot_table
@app.route("/pivot_table", methods=['POST', 'GET'])
def pivot_table():
	title = "Pivot Table"
	template_vars = {
		"title": title
	}

	# Get input from pivot_table_builder
	row = request.form['row']
	col = request.form['col']
	values = request.form['data']
	filter_data = request.form['filter data']
	filter_method = request.form['sign']
	agg = request.form['agg']
	filter_value = request.form['Filter_value']

	# Filter dataset
	if(filter_data != "No Filter"):
		filteredData = filterData(filter_data, filter_value, filter_method)
	else:
		filteredData = dataset

	
	with open('templates/pivot_table.html' , 'w') as html:
		html.write('''
			{% extends "base.html" %}

			{% block customCSS %}   
			<link rel="stylesheet" href="templates/css/pivottable.css" type="text/css">
                 <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap.min.css">
			{% endblock %}

			{% block content %}
			''')

		try:
			# Create pivot table
			table = constructPT(filteredData, row, col, values, agg)

			# Get table maximum value
  			maxVal=table.max().max()

  			# Set colour level 
  			vPoor=int(float(maxVal/5))
  			poor=vPoor*2
     			avg=vPoor*3
  			good=vPoor*4
  			vGood=vPoor*5        
                     
			c = table.to_html()
			c = c.encode('ascii', 'ignore')           
			html.write('''
<script src="http://code.jquery.com/jquery-1.8.3.js"></script>
<script src="http://code.jquery.com/mobile/1.2.0/jquery.mobile-1.2.0.min.js"></script>                    
<script type="text/javascript">
$('tbody tr td').each(

function() {
    var ''')
     # Write colour level into html file 
			html.write('vGood = '+ str(vGood)+',')
			html.write('good = '+ str(good)+',')
			html.write('avg = '+ str(avg)+',')
			html.write('poor= '+ str(poor)+',')
			html.write('vPoor= '+ str(vPoor)+',')
			html.write('''
        score = $(this).text();
    
    if (score >= vGood) {
        $(this).addClass('vGood');
    }
    else if (score < vGood && score >= good) {
        $(this).addClass('good');
    }
    else if (score <good && score >= avg) {
        $(this).addClass('avg');
    }
    else if (score < avg&& score >= poor) {
        $(this).addClass('poor');
    }
    else if (score < poor) {
        $(this).addClass('vPoor');
    }
    });
 </script>''')
 			html.write('''<h1>Pivot Table</h1><br><br>''')
 			html.write('<table>'+c +'<br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>')
 		# If user input invalid
		except:
			html.write('''<h1>Error</h1><br><br><br><br><br><br><br><br><br><br>
					<h2 style="text-align:center">INVALID INPUT! Please check your selection. </h2>''')

		html.write('''
			{% endblock %}
		''')

	return render_template("pivot_table.html",vars=template_vars)


# Get colour 
def getColoredRow(maxVal,val):
    white = [255,255,255]
    orange = [255,63,0]
    red = white[ 0 ] + ((orange[0] - white[0] ) * val / maxVal )
    green = white[ 1 ] + ((orange[1] - white[1] ) * val / maxVal )
    blue = white[ 2 ] + ((orange[2] - white[2] ) * val / maxVal )
    
    color = '<td style="background-color: rgb(%s,%s,%s)">%s</td>;'%(red,green,blue,val)
    return color