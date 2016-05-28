from flask import render_template
from phase3 import app
import csv

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
            {% extends "base.html" %}

            {% block customCSS %}
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <link rel="stylesheet" type=text/css href="templates/stylesheets/dataset.css">


            <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/bootstrap-table/1.10.1/bootstrap-table-locale-all.js">


            <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/bootstrap-table/1.10.1/bootstrap-table.min.css">

            <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css">
            <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.2/jquery.min.js"></script>
            <script src="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/js/bootstrap.min.js"></script>
            {% endblock %}

            {% block header %}
            <div class="header-content">
                <img src="templates/img/car_accident_icon.png" alt="car accident icon">
                <div class="header-title">
                    <h2>Road Accidents</h2>
                    <p>Leeds, England 2012</p>
                </div>
            </div>
            {% endblock %}''')    
        html.write('{% block content %}\r')
        html.write('<div class="table-responsive">\r <table data-toggle = "table" data-pagination = "true" id = "table">\r')
        r = 0
        for row in csvData:
            if r == 0:
                html.write('\t<thead>\r\t\t<tr>\r')
                for col in row:
                    html.write('\t\t\t<th data-sortable="true" >' + col + '</th>\r')
                html.write('\t\t</tr>\r\t</thead>\r')
                html.write('\t<tbody>\r')
            else:
                html.write('\t\t<tr>\r')
                for col in row:
                    html.write('\t\t\t<td>' + col + '</td>\r')
                html.write('\t\t</tr>\r')

            r += 1
        html.write('\t</tbody>\r')
        html.write('</table>\r <\div>\r')
        html.write('{% endblock %}\r')
        
        html.write('''
            {% block customJS %}

            <!-- jQuery (necessary for Bootstrap's JavaScript plugins) -->
            <script src="https://ajax.googleapis.com/ajax/libs/jquery/2.1.0/jquery.min.js"></script>

            <!-- Latest compiled and minified JavaScript -->
            <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/js/bootstrap.min.js"></script>

            <!-- Latest compiled and minified JavaScript -->
            <script src="https://cdnjs.cloudflare.com/ajax/libs/bootstrap-table/1.9.0/bootstrap-table.min.js"></script>
            
            {% endblock %}
            ''')


    return render_template("dataset.html",vars=template_vars)
