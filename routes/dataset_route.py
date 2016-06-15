from flask import render_template
from phase3 import app
import csv

#This page contains the dataset table that we used for our analysis. Python is
#used to construct the csv file into a table with Bootstrap.

csvFile = open('data_2012.csv',encoding = 'utf-8')
csvReader = csv.reader(csvFile)
csvData = list(csvReader)

#server/dataset
@app.route("/dataset")
def dataset():
    title = "Dataset"
    template_vars = {
        "title": title
    }
    with open('templates/dataset.html', 'w',encoding = 'utf-8') as html: #enter the output filename
        html.write('''
            {% extends "base.html" %}

            {% block customCSS %}

            <!-- For Webpage and Table styling -->
            <link rel="stylesheet" href="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css">
            <link rel="stylesheet" type=text/css href="templates/stylesheets/dataset.css">
          
            {% endblock %}

            {% block header %}

            <div class="header-content">
                <img src="templates/img/car_accident_icon.png" alt="car accident icon">
                <div class="header-title">
                    <h2>Road Accidents</h2>
                    <p>Leeds, England 2012</p>
                </div>
            </div>

            <div id="myBar">
                <div id="label">Loading...</div>
            </div>
            {% endblock %}''')    
        html.write('{% block content %}\r')

        # constructs table
        html.write('<div id = "body" style = "display:none;">\r')
        html.write('<table data-toggle = "table" data-pagination = "true" id = "table" data-search="true">\r')
        r = 0
        for row in csvData:
            if r == 0: 
                # create headers
                html.write('\t<thead class= table_header>\r\t\t<tr>\r')
                for col in row:
                    html.write('\t\t\t<th data-sortable="true" class=table_col>' + col + '</th>\r')
                html.write('\t\t</tr>\r\t</thead>\r')
                html.write('\t<tbody>\r')
            else:
                # put in data
                html.write('\t\t<tr>\r')
                for col in row:
                    html.write('\t\t\t<td>' + col + '</td>\r')
                html.write('\t\t</tr>\r')
            r += 1
        html.write('\t</tbody>\r')
        html.write('</table>\r</div>\r')
        html.write('{% endblock %}\r')
        
        html.write('''
            {% block customJS %}

            <!-- For Table Styling and interactive-->            
            <script src="http://code.jquery.com/jquery.min.js"></script>

            <!-- jQuery (necessary for Bootstrap's JavaScript plugins) -->
            <script src="https://ajax.googleapis.com/ajax/libs/jquery/2.1.0/jquery.min.js"></script>

            <!-- Latest compiled and minified JavaScript -->
            <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/js/bootstrap.min.js"></script>

            <!-- Latest compiled and minified JavaScript -->
            <script src="https://cdnjs.cloudflare.com/ajax/libs/bootstrap-table/1.9.0/bootstrap-table.min.js"></script>

            <script type="text/javascript">
            jQuery(document).ready(function(){
                $('#body').show();
                $('#myBar').hide();
            });
            </script>
            
            {% endblock %}
            ''')


    return render_template("dataset.html",vars=template_vars)