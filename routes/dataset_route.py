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

    # content = open('data_2012.csv')
    # reader = csv.reader(content)
    # headers = reader.next()
    # data = zip(*reader)
    # numerical_headers = []
    # count = 0
    # for column in data:
    #     if column[1].isdigit():
    #         numerical_headers.append(headers[count])
    #     count += 1


    # elements_list = pivot_table_builder_route.getelements("data_2012.csv")
    # numerical_elements = elements_list[0]

    with open('templates/dataset.html', 'w') as html: #enter the output filename
        html.write('''
            {% extends "base.html" %}

            {% block customCSS %}
          
            <link rel="stylesheet" type=text/css href="templates/stylesheets/dataset.css">

            <!--link rel="stylesheet" href="https://rawgit.com/wenzhixin/bootstrap-table/master/src/bootstrap-table.css"-->

            <!--script src="https://rawgit.com/wenzhixin/bootstrap-table/master/src/bootstrap-table.js"></script-->

            <script src="templates/stylesheets/dataset.js"></script>

            


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
        html.write('<table data-toggle = "table" data-pagination = "true" id = "table" data-search="true">\r')
        r = 0
        for row in csvData:
            if r == 0:
                html.write('\t<thead class= table_header>\r\t\t<tr>\r')
                for col in row:
                    # if col in numerical_headers:
                    #     html.write('\t\t\t<th data-sortable="true" class=s_table_col>' + col + '</th>\r')
                    # else:
                    #     html.write('\t\t\t<th data-sortable="true" class=table_col>' + col + '</th>\r')
                    html.write('\t\t\t<th data-sortable="true" class=table_col>' + col + '</th>\r')
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