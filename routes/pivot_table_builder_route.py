from flask import render_template
from phase3 import app
import csv


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

            {% block customCSS %}
                <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/bootstrap-select/1.10.0/css/bootstrap-select.min.css"><!--found-->
                <link rel="stylesheet" href="templates/css/pivot_table_builder.css" type="text/css">
                <meta name="viewport" content="width=device-width, initial-scale=1"><!--found-->
                <link rel="stylesheet" href="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css"><!--found-->
            {% endblock %}

            {% block customJS %}
                <script src="https://ajax.googleapis.com/ajax/libs/jquery/2.2.2/jquery.min.js"></script>
                <!-- Latest compiled and minified JavaScript -->
                <script src="https://cdnjs.cloudflare.com/ajax/libs/bootstrap-select/1.10.0/js/bootstrap-select.min.js"></script> <!--found-->
                <!-- (Optional) Latest compiled and minified JavaScript translation files -->
                <script src="https://cdnjs.cloudflare.com/ajax/libs/bootstrap-select/1.10.0/js/i18n/defaults-*.min.js"></script><!--found-->
                <script src="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/js/bootstrap.min.js"></script><!--found-->
            {% endblock %}  
        ''')

        html.write('{% block content %}')

        html.write('<form method="post" action="pivot_table">')

        # rows
        html.write('''
            <!--Row-->
            <div class="row" id='dropbox1'>
                <div class="col-xs-6 form-group">

                  <div class = 'row'><label for = "row_label"> Row </label></div>
                
                  <div class="row">
                  <select class="selectpicker show-menu-arrow" name="row" id="row">
        ''')
        for e in categorical_elements:
            html.write("<option value='%s'>%s</option>"%(e,e))

        html.write('''
                </select>
                </div>
            </div>
        ''')

        # columns
        html.write('''
            <!--Column-->
            <div class="col-xs-6 form-group">
                <div class="row"><label for = "col_label"> Column </label></div>
                <div class="row">
                <select class="selectpicker show-menu-arrow" name="col" id="col">
        ''')
        for e in categorical_elements:
            html.write("<option value='%s'>%s</option>"%(e,e))

        html.write('''
                </select>
            </div>
          </div>
        </div>
        ''')

        # aggregation category
        html.write('''
            <!--Values-->
            <div class="row" id='dropbox2'>
            <div class="col-xs-6 form-group">
              <div class="row"> <label for = "agg_label"> Aggregation </label> </div>
              <div class="row">
                <select class="selectpicker show-menu-arrow" name="data" id="data">
        ''')
        
        for e in numerical_elements:
            html.write("<option value='%s'>%s</option>"%(e,e))
        
        html.write('''
                </select>
            </div>
        ''')

        #aggregation method
        html.write('''
            <!--Aggregation-->
            <div class="row">
                <select class="selectpicker show-menu-arrow" name="agg" id="agg">
                    <option value="sum">Sum</option>
                    <option value="median">Median</option>
                    <option value="maximum">Maximum</option>
                    <option value="minimum">Minimum</option>
                    <option value="mean">Mean</option>
                </select>
                </div>
            </div>
        ''')

        # filter category
        html.write('''
            <!--Filter-->
            <div class="col-xs-6 form-group">
                <div class="row"> <label for = "filter_label"> Report Filter </label> </div>
                <div class="row">
                    <select class="selectpicker show-menu-arrow" name="filter data" id="filter data">
        ''')
        filter_elements=["No Filter"]+all_elements
        for e in filter_elements:
            html.write("<option value='%s'>%s</option>"%(e,e))

        html.write('''
                </select>
            </div>
        ''')

        # filter method
        html.write('''
            <div class="row"> 
                <select class="selectpicker show-menu-arrow" name="sign" id="sign">
                  <option value="=">equal to</option>
                  <option value="<">not equal to</option>
                  <option value=">">greater than</option>
                  <option value=">=">equal to or greater than</option>
                  <option value="<">less than</option>
                  <option value="<=">equal to or less than</option>
                </select>
            
        ''')

        #filter value
        html.write('''
                <div class="row">
                <input type="text" name = "Filter_value"/>
                </div>
            </div>
        ''')

        # submit
        html.write('''
            </div>
            <p>
                <input type="submit" />
            </p>
        </div>
        </form>
        ''')
        html.write('{% endblock %}')
    return render_template("pivot_table_builder.html",vars=template_vars)


def getelements(filename):
    content = open(filename)
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
