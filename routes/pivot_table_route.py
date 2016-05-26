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
			<link rel="stylesheet" href="templates/css/pivottable.css" type="text/css">
                 <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap.min.css">
			{% endblock %}

			{% block content %}
			''')

		try:
			table = constructPT(filteredData, row, col, values, agg)
  			maxVal=table.max().max()
  			vPoor=int(float(maxVal/5))
  			poor=vPoor*2
     			avg=vPoor*3
  			good=vPoor*4
  			vGood=vPoor*5        
			# # table = table.drop('All', axis=1)
	 	# # 	table = table.drop('All')
	 		# r = 0;
	 		# for row in table.iterrows():
	 		# 	if r == 0:
	 		# 		html.write('\t<thead>\r\t\t<tr>\r')
				# for col in row:
				# 	html.write('\t\t\t<th data-sortable="true">' + col + '</th>\r')
				# 	html.write('\t\t</tr>\r\t</thead>\r')
				# 	html.write('\t<tbody>\r')
	 		# 		#put headers in right pose
	 		# 		r = 1;
	 		# 	else: 
	 		# 		#deal with data
	 		# 		for cell in row:
	 		# 			val = row[cell]
	 		# 			getColoredRow(maxVal, val)
                     
			c = table.to_html()
			c = c.encode('ascii', 'ignore')           
			html.write('''
<script src="http://code.jquery.com/jquery-1.8.3.js"></script>
<script src="http://code.jquery.com/mobile/1.2.0/jquery.mobile-1.2.0.min.js"></script>                    
<script type="text/javascript">
$('tbody tr td').each(

function() {
    var ''') 
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
		except:
			html.write('''<h1>Error</h1><br><br><br><br><br><br><br><br><br><br>
					<h2 style="text-align:center">INVALID INPUT! Please check your selection. </h2>''')
		
		# c = table.to_html()
		# c = c.encode('ascii', 'ignore')
		# html.write(c)

		html.write('''
			{% endblock %}
		''')

	return render_template("pivot_table.html",vars=template_vars)


def getColoredRow(maxVal,val):
    white = [255,255,255]
    orange = [255,63,0]
    red = white[ 0 ] + ((orange[0] - white[0] ) * val / maxVal )
    green = white[ 1 ] + ((orange[1] - white[1] ) * val / maxVal )
    blue = white[ 2 ] + ((orange[2] - white[2] ) * val / maxVal )
    
    color = '<td style="background-color: rgb(%s,%s,%s)">%s</td>;'%(red,green,blue,val)
    return color



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
        
#       table = table.drop('All', axis=1)
#       table = table.drop('All')
#       maxVal = table.values.max()
#       c = table.to_csv(column=False)
#       r = 0
#       for row in c:
#           if r == 0:
#               html.write('\t<thead>\r\t\t<tr>\r')
#               for col in row:
#                   html.write('\t\t\t<th data-sortable="true">' + col + '</th>\r')
#                   html.write('\t\t</tr>\r\t</thead>\r')
#                   html.write('\t<tbody>\r')
#           else:
#               html.write('\t\t<tr>\r')
#               for col in row:
#                   html.write('\t\t\t<td>' + col + '</td>\r')
#                   html.write('\t\t</tr>\r')
#           r += 1
#       html.write('\t</tbody>\r')
#       html.write('</table>\r')

#       html.write('''
#           {% endblock %}
#       ''')

#   return render_template("pivot_table.html",vars=template_vars)



    # filterCategory = request.form['Filter Category']
    # filterMethod = request.form['Filter Method']
    # filterValue = request.form['Filter Value']
    # row = request.form['Row']
    # column = request.form['Column']
    # agg = request.form['agg']
    # values = request.form['Values']
    # filteredData = filterData(filterCategory,filterValue,filterMethod)
    # table = constructPT(filteredData,row,column,values,agg)
