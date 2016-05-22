from flask import render_template
from phase3 import app
import csv

def getelements(filename):
    content = open("data_2012.csv")
    reader = csv.reader(content)
    headers = reader.next()
    data = zip(*reader)
    categorical_headers= []
    numerical_headers= []
    header_type = []
    count= 0
    for column in data:
        if column[1].isdigit():
            numerical_headers.append(headers[count])
        else:
            categorical_headers.append(headers[count])
        count +=1
    header_type.append(numerical_headers)
    header_type.append(categorical_headers)
    return header_type

#server/pivot_table_builder
@app.route("/pivot_table_builder")
def pivot_table_builder():
    title = "Pivot Table"
    template_vars = {
      "title": title
    }
    elements_list = getelements("data_2012.csv")
    all_elements = elements_list[0]+elements_list[1]
    categorical_elements = elements_list[1]
    numerical_elements = elements_list[0]
    with open('templates/pivot_table_builder.html' , 'w') as html:
        html.write('''
            {% extends "base.html" %}

            {% block content %}
            <form method="post" action="pivot_table">

            <!--Filter-->
              <p>Filter Category:
                <select name="Filter Category">
        ''')
        for e in all_elements:
            html.write("<option value='%s'>%s</option>"%(e,e))

        html.write('''
                </select>
              </p>
              <p>Filter Method:
                <select name="Filter Method">
                  <option value="=">equal to</option>
                  <option value="<">not equal to</option>
                  <option value=">">greater than</option>
                  <option value=">=">equal to or greater than</option>
                  <option value="<">less than</option>
                  <option value="<=">equal to or less than</option>
                </select>
              </p>
              <p>Filter Value:
                <textarea name="Filter Value"></textarea>
              </p>

            <!--Row-->
            <p>Row:
                <select name="Row">
        ''')
        for e in categorical_elements:
            html.write("<option value='%s'>%s</option>"%(e,e))

        html.write('''
                </select>
              </p>
            <!--Column-->
            <p>Column:
                <select name="Column">
        ''')
        for e in categorical_elements:
            html.write("<option value='%s'>%s</option>"%(e,e))

        html.write('''
                </select>
              </p>
            <!--Values-->
            <p>Values:
                <select name="Values">
        ''')
        for e in numerical_elements:
            html.write("<option value='%s'>%s</option>"%(e,e))

        html.write('''
                </select>
              </p>
            <!--Aggregation-->
            <p>Aggregation Method:
                <select name="agg">
                  <option value="sum">sum</option>
                  <option value="median">median</option>
                  <option value="maximum">maximum</option>
                  <option value="minimum">minimum</option>
                  <option value="mean">mean</option>
                </select>
              </p>
              <p>
                <input type="submit" />
              </p>
            </form>
            {% endblock %}
        ''')
    return render_template("pivot_table_builder.html",vars=template_vars)

# #server/pivot_table_builder
# @app.route("/pivot_table_builder")
# def pivot_table_builder():
# 	with open('templates/pivot_table_builder.html' , 'w') as html:
# 		html.write('''
# 		<!DOCTYPE html>
# 		<html lang="en">
#   		<head>
#   		<meta charset="utf-8">
#   		<title>Pivot Table Builder</title>

# 		<link href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.2/css/bootstrap.min.css" rel="stylesheet"/>
# 		<!-- Latest compiled and minified CSS -->
# 		<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/bootstrap-select/1.10.0/css/bootstrap-select.min.css">
# 		<link rel="stylesheet" href="templates/css/pivot_table_builder.css" type="text/css">
# 		<meta name="viewport" content="width=device-width, initial-scale=1">
# 		<link rel="stylesheet" href="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css">
#   		<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.2/jquery.min.js"></script>
	
#   		</head>
#   		<h1>Pivot Table</h1>
#   		''')
#   		html.write('''
# 		<body>
# 		<div class="row" id='dropbox1'>
# 			<div class="col-xs-6 form-group">
# 				<label for = "row_label"> Row Label </label>
# 				<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.7.2/jquery.min.js"></script>
# 				<form action = "templates/pivot_table.html" method = "GET">
# 				<select class="selectpicker show-menu-arrow" name="row" id="row">
# 					<option value="none" selected>Select Row Label</option>
# 		''')
# 		headers = readdata.cate_header("data_2012.csv")
# 		for header in headers:
#   			html.write('\t\t\t\t\t<option value="' + header + '">' + header + '</option>\r')
# 		html.write('''
# 				</select></form>
# 			</div>
# 			<div class="col-xs-6 form-group">
# 				<label for = "col_label"> Column Label </label>
# 				<form action = "templates/pivot_table.html" method = "GET">
# 				<select class="selectpicker show-menu-arrow" name="col" id="col">
# 					<option value="none" selected>Select Column Label</option>
# 		''')
# 		headers = readdata.cate_header("data_2012.csv")
# 		for header in headers:
#   			html.write('\t\t\t\t\t<option value="' + header + '">' + header + '</option>\r')
# 		html.write('''
# 				</select></form>
# 			</div>
# 		</div>
# 	    <div class="row" id='dropbox2'>
# 			<div class="col-xs-6 form-group">
# 				<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.7.2/jquery.min.js"></script>
# 				<label for = "agg_label"> Aggregation </label>
# 				<form action = "templates/pivot_table.html" method = "GET">
# 				<select class="selectpicker show-menu-arrow" name="data" id="data">
# 					<option value="none" selected>Select Aggregation</option>
# 		''')
# 		headers = readdata.num_header("data_2012.csv")
# 		for header in headers:
#   			html.write('\t\t\t\t\t<option value="' + header + '">' + header + '</option>\r')
# 		html.write('''
# 				</select></form>
# 			</div>
# 			<div class="col-xs-6 form-group">
# 				<label for = "filter_label"> Report Filter </label>
# 				<form action = "templates/pivot_table.html" method = "GET">
# 				<select class="selectpicker show-menu-arrow" name="filter" id="filter">
# 					<option value="none" selected>Select Filter Data</option>
# 		''')
# 		headers = readdata.cate_header("data_2012.csv") + readdata.num_header("data_2012.csv")
# 		for header in headers:
#   			html.write('\t\t\t\t\t<option value="' + header + '">' + header + '</option>\r')
# 		html.write('''
# 				</select></form>
# 			</div>

# 			<script src="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/js/bootstrap.min.js"></script>
# 			<a href="/pivot_table" class="btn btn-info btn-lg">Get Pivot Table</a>
# 		</div>
# 		</div>
# 		<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.2/jquery.min.js"></script>
# 		<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.2/js/bootstrap.min.js"></script>
# 		<!-- Latest compiled and minified JavaScript -->
# 		<script src="https://cdnjs.cloudflare.com/ajax/libs/bootstrap-select/1.10.0/js/bootstrap-select.min.js"></script>
# 		<!-- (Optional) Latest compiled and minified JavaScript translation files -->
# 		<script src="https://cdnjs.cloudflare.com/ajax/libs/bootstrap-select/1.10.0/js/i18n/defaults-*.min.js"></script>

# 		</body>
# 		</html>
# 			''')
# 	return render_template("pivot_table_builder.html")

# @app.route("/pivot_table", methods=['POST'])
# def getSelection():
# 	row = request.form.get('row')
# 	col = request.form.get('col')
# 	# if request.Post:
# 	# 	row = request.get_all(row)
# 	# 	col = request.get_all(col)
# 	print row
# 	print col
# 	return redirect('/')