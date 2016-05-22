from flask import render_template, request
from phase3 import app
import pandas as pd
import numpy as np

# Import modules for CGI handling 
import cgi, cgitb 

# Create instance of FieldStorage 
# form = cgi.FieldStorage() 
# cgitb.enable()

#server/pviot_table
#@app.route("/pivot_table")
@app.route("/pivot_table", methods = ['POST','GET'])
def pivot_table():
	with open('templates/pivot_table.html' , 'w') as html:
		body = '''
<!DOCTYPE html>
<html lang="en">
	<head>
	<meta charset="utf-8">
	<title>Pivot Table</title>
	</head>
	<body>
	<div id="row"><p>The row is: %s</p></div>
	<div id="col"><p>The col is: %s</p></div>
	<div id="data"><p>The data is: %s</p></div>
	<div id="filter"><p>The filter is: %s</p></div>
	<div id="sign"><p>The sign is: %s</p></div>
	<div id="filter_value"><p>The filter_value is: %s</p></div>
				'''
		# row = request.form['row']
		# col = request.form['col']
		# data = request.form['data']
		# filter = request.form['filter']
		# sign = request.form['sign']
		# filter_value = request.form['filter_value']

		row = request.form.get("row")
		col = request.form.get('col')
		data = request.form.get('data')
		filter = request.form.get('filter')
		sign = request.form.get('sign')
		filter_value = request.form.get('filter_value')

		# row = form.getvalue('row')
		# col = form.getvalue('col')
		# data = form.getvalue('data')
		# filter = form.getvalue('filter')
		# sign = form.getvalue('sign')
		# filter_value = form.getvalue('filter_value')

	# row = request.args.get('row')
	# col = request.args.get('col')
	# data = request.args.get('data')
	# filter = request.args.get('filter')


		body = body % (row, col, data, filter, sign, filter_value)
		body += '''
	</body>
</html>
			'''
		#print body

		html.write(body)
	return render_template("pivot_table.html")



