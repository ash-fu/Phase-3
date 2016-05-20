from flask import Flask, render_template, request
from phase3 import app
import csv
import pandas as pd
import numpy as np
import jinja2
import readdata

csvFile = open('data_2012.csv')#enter the csv filename
csvReader = csv.reader(csvFile)
csvData = list(csvReader)

#server/dataset
@app.route("/dataset")
def dataset():
    title = "Dataset"
    template_vars = {
        "title": title
    }
    with open('templates/dataset.html', 'w') as html: #enter the output filename
	    html.write('''
	<head>
		<meta charset="utf-8">

		<title>Dataset</title>

		<link rel="stylesheet" href="templates/stylesheets/dataset.css" type="text/css">

		<link rel="stylesheet" href="templates/css/bootstrap-table.min.css" type="text/css">

		<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap.min.css">
	
	</head>	
		''')   
	    html.write('''
<body>
	<header>
	    <div class="header-content">
	    	<img src="templates/img/car_accident_icon.png" alt="car accident icon">
	    	<div class="header-title">
	    		<h2>Road Accidents</h2>
	    		<p>Leeds, England 2012</p>
	    	</div>
	    </div>
	</header>
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
    return render_template("dataset.html",vars=template_vars)
    