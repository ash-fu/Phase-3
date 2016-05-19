from flask import Flask, render_template
from phase3 import app
import csv

csvFile = open('data_2012.csv')#enter the csv filename
csvReader = csv.reader(csvFile)
csvData = list(csvReader)

#holds all routes to the application

#server/
@app.route("/")
def index():
    return render_template("index.html")

#server/pivot_table_builder
@app.route("/pivot_table_builder")
def pivot_table_builder():
	return render_template("pivot_table_builder.html")

#server/dataset
@app.route("/dataset")
def dataset():
	with open('templates/dataset.html', 'w') as html: #enter the output filename
	    html.write('''
	<head>

		<title>Dataset</title>

		<link rel="stylesheet" href="templates/css/bootstrap-table.min.css" type="text/css">

		<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap.min.css">
	
	</head>	
		''')   
	    html.write('''
	    	<body>
	    	<table data-toggle = "table" data-pagination = "true">\r''')

	    r = 0
	    for row in csvData:
	        if r == 0:
	            html.write('\t<thead>\r\t\t<tr>\r')
	            for col in row:
	                html.write('\t\t\t<th data-sortable="true">' + col + '</th>\r')
	            html.write('\t\t</tr>\r\t</thead>\r')
	            html.write('\t<tbody>\r')
	        else:
	            html.write('\t\t<tr>\r')
	            for col in row:
	                html.write('\t\t\t<td>' + col + '</td>\r')
	            html.write('\t\t</tr>\r')

	        r += 1
	    html.write('\t</tbody>\r')
	    html.write('</table>\r')
	    html.write('</body>\r')
	    html.write('''
		<!-- jQuery (necessary for Bootstrap's JavaScript plugins) -->
		<script src="https://ajax.googleapis.com/ajax/libs/jquery/2.1.0/jquery.min.js"></script>

		<!-- Latest compiled and minified JavaScript -->
		<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/js/bootstrap.min.js"></script>

		<!-- Latest compiled and minified JavaScript -->
		<script src="https://cdnjs.cloudflare.com/ajax/libs/bootstrap-table/1.8.1/bootstrap-table.min.js"></script>
		''') 
	return render_template("dataset.html")