# coding=utf-8
from flask import render_template, request
from phase3 import app
import pandas as pd
import numpy as np
import csv
import StringIO
from processPT import *
from readdata import *

dataset = pd.read_csv("data_2012.csv")
dataset.head()
content = open("data_2012.csv")
reader = csv.reader(content)
header = reader.next();

#server/pivot_table
@app.route("/pivot_table", methods=['POST', 'GET'])
def pivot_table():
    title = "Pivot Table"
    template_vars = {
        "title": title
    }
    row = request.form['row']
    col = request.form['col']
    values = request.form['val']
    agg = request.form['agg']
    filter_category = request.form['filter category']
    filter_method = request.form['filter method']
    filter_value = request.form['filter value']  
    headers = getelements("data_2012.csv")

    with open('templates/pivot_table.html' , 'w') as html:
        html.write('''
            {% extends "base.html" %}

            {% block customCSS %}
            <link rel="stylesheet" href="templates/stylesheets/dataset.css" type="text/css">
            <link rel="stylesheet" href="templates/css/bootstrap-table.min.css" type="text/css">
            <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap.min.css">            
            {% endblock %}

            {% block customJS %}
            <!-- jQuery (necessary for Bootstrap's JavaScript plugins) -->
            <script src="https://ajax.googleapis.com/ajax/libs/jquery/2.1.0/jquery.min.js"></script>
            <!-- Latest compiled and minified JavaScript -->
            <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/js/bootstrap.min.js"></script>
            <!-- Latest compiled and minified JavaScript -->
            <script src="https://cdnjs.cloudflare.com/ajax/libs/bootstrap-table/1.8.1/bootstrap-table.min.js"></script>
            {% endblock %}
            ''')
        try:
            filteredData = filterData(filter_category, filter_value, filter_method,headers)
            table = constructPT(filteredData, row, col, values, agg)
            table = table.drop('All', axis=1)
            table = table.drop('All')
            maxVal = table.values.max()

            c = table.to_csv()
            reader = csv.reader(c.split('\n'), delimiter=',')
            csvData = list(reader)
            csvData.pop()

            html.write('''
                {% block header %}

                <h2>Pivot Table Builder</h2>

                {% endblock %}
            ''')

            html.write("{% block content %}")

            html.write('<div style="overflow:scroll;height:400px" >')
            html.write('<table  style="width:900px" class="table">\r')
            r = 0
            for row in csvData:
                if r == 0:
                    html.write('\t<thead>\r\t\t<tr>\r')
                    for col in row:
                        html.write('\t\t\t<th>' + col + '</th>\r')
                    html.write('\t\t</tr>\r\t</thead>\r')
                    html.write('\t<tbody>\r')
                else:
                    html.write('\t\t<tr>\r')
                    for col in row:
                        html.write(getColoredRow(maxVal,col))
                    html.write('\t\t</tr>\r')

                r += 1
            html.write('\t</tbody>\r')
            html.write('</table>\r')
            html.write('</div>')
        except:
            html.write("{% block content %}")
            html.write('''
                <p>Error:No results</p>
                <a href="/pivot_table_builder">Go Back To Builder</a>
            ''')

        html.write("{% endblock %}")

    return render_template("pivot_table.html",vars=template_vars)

