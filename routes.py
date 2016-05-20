from flask import Flask, render_template, request
from phase3 import app
import csv
import pandas as pd
import numpy as np
import jinja2

csvFile = open('data_2012.csv')#enter the csv filename
csvReader = csv.reader(csvFile)
csvData = list(csvReader)

#holds all routes to the application

#server/
@app.route("/")
def index():
	title = "Traffic Accident Statistics"
	template_vars = {
		"title": title
	}
	return render_template("index.html",vars=template_vars)


#server/
@app.route("/findings")
def findings():
    title = "Findings"
    template_vars = {
        "title": title
    }
    return render_template("findings.html",vars=template_vars)

#server/pivot_table_builder
@app.route("/pivot_table_builder")
def pivot_table_builder():
	with open('templates/pivot_table_builder.html' , 'w') as html:
		html.write('''
		<!DOCTYPE html>
		<html lang="en">
  		<head>
  		<meta charset="utf-8">
  		<title>Pivot Table Builder</title>

		<link href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.2/css/bootstrap.min.css" rel="stylesheet"/>
		<!-- Latest compiled and minified CSS -->
		<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/bootstrap-select/1.10.0/css/bootstrap-select.min.css">
		<link rel="stylesheet" href="templates/css/pivot_table.css" type="text/css">
		  <meta name="viewport" content="width=device-width, initial-scale=1">
  		<link rel="stylesheet" href="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css">
  		<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.2/jquery.min.js"></script>

  		</head>
  		<h1>Pivot Table</h1>
  		''')
  		html.write('''
		<body>
		<div class="row" id='dropbox1'>
			<div class="col-xs-6 form-group">
				<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.7.2/jquery.min.js"></script>
				<form action = "/" method = "post">
				<select class="selectpicker show-menu-arrow" name="row" id="row">
					<option value="none" selected>Select Row Label</option>
		''')
		headers = readdata.cate_header("data_2012.csv")
		for header in headers:
  			html.write('\t\t\t\t\t<option value="' + header + '">' + header + '</option>\r')
		html.write('''
				</select></form>
			</div>
			<div class="col-xs-6 form-group">
				<form action = "/" method = "post">
				<select class="selectpicker show-menu-arrow" name="col" id="col">
					<option value="none" selected>Select Column Label</option>
		''')
		headers = readdata.cate_header("data_2012.csv")
		for header in headers:
  			html.write('\t\t\t\t\t<option value="' + header + '">' + header + '</option>\r')
		html.write('''
				</select></form>
			</div>
		</div>
	    <div class="row" id='dropbox2'>
			<div class="col-xs-6 form-group">
				<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.7.2/jquery.min.js"></script>
				<form action = "/" method = "post">
				<select class="selectpicker show-menu-arrow" name="data" id="data">
					<option value="none" selected>Select Aggregation</option>
		''')
		headers = readdata.num_header("data_2012.csv")
		for header in headers:
  			html.write('\t\t\t\t\t<option value="' + header + '">' + header + '</option>\r')
		html.write('''
				</select></form>
			</div>
			<div class="col-xs-6 form-group">
				<form action = "/" method = "post">
				<select class="selectpicker show-menu-arrow" name="filter" id="filter">
					<option value="none" selected>Select Filter Data</option>
		''')
		headers = readdata.cate_header("data_2012.csv") + readdata.num_header("data_2012.csv")
		for header in headers:
  			html.write('\t\t\t\t\t<option value="' + header + '">' + header + '</option>\r')
		html.write('''
				</select></form>
			</div>


			<script src="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/js/bootstrap.min.js"></script>
			<a href="/pivot_table" class="btn btn-info btn-lg">Get Pivot Table</a>
		</div>
		</div>
		<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.2/jquery.min.js"></script>
		<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.2/js/bootstrap.min.js"></script>
		<!-- Latest compiled and minified JavaScript -->
		<script src="https://cdnjs.cloudflare.com/ajax/libs/bootstrap-select/1.10.0/js/bootstrap-select.min.js"></script>

		<!-- (Optional) Latest compiled and minified JavaScript translation files -->
		<script src="https://cdnjs.cloudflare.com/ajax/libs/bootstrap-select/1.10.0/js/i18n/defaults-*.min.js"></script>

		<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.2/jquery.min.js" type="text/javascript">
			var row = document.getElementById("row");
			var col = document.getElementById("col");
			dataset = csvData;
			agg = "sum";
			table = constructPT(dataset,row,col,values,agg);
			pivot_table(table);
		</script>

		</body>
		</html>
			''')
	return render_template("pivot_table_builder.html")

@app.route("/getSelection", methods=['GET','POST'])
def getSelection():
	row = request.form.get('row')
	col = request.form.get('col')
	# if request.Post:
	# 	row = request.get_all(row)
	# 	col = request.get_all(col)
	print row
	print col
	return (row,col)


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

