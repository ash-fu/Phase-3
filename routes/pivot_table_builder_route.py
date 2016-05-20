from flask import render_template
from phase3 import app
import readdata

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