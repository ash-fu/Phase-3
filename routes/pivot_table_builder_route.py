from flask import render_template
from phase3 import app
import csv
from readdata import *

#server/pivot_table_builder
@app.route("/pivot_table_builder")
def pivot_table_builder():
    title = "Pivot Table"
    template_vars = {
      "title": title
    }
    elements_list = getelements("data_2012.csv")
    all_elements = elements_list[0]+elements_list[1]
    filter_elements=["No Filter"]+all_elements
    categorical_elements = elements_list[1]
    numerical_elements = elements_list[0]


    with open('templates/pivot_table_builder.html' , 'w') as html:
        html.write('''
            {% extends "base.html" %}

            {% block customCSS %}
                <link href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.2/css/bootstrap.min.css" rel="stylesheet"/>
                <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/bootstrap-select/1.10.0/css/bootstrap-select.min.css">
                <link rel="stylesheet" href="templates/css/pivot_table_builder.css" type="text/css">
                <link rel="stylesheet" href="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css">
            {% endblock %}

            {% block customJS %}
                <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.2/jquery.min.js"></script>
                <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.2/js/bootstrap.min.js"></script>
                <script src="https://cdnjs.cloudflare.com/ajax/libs/bootstrap-select/1.10.0/js/bootstrap-select.min.js"></script>
                <script src="https://cdnjs.cloudflare.com/ajax/libs/bootstrap-select/1.10.0/js/i18n/defaults-*.min.js"></script>
                <script src="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/js/bootstrap.min.js"></script>   
                <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.0/jquery.min.js"></script>
                <script src="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/js/bootstrap.min.js"></script>
            {% endblock %}  
        ''')

        html.write('{% block header %}')
        html.write('''
        <div id = "heading">
            <h2>Pivot Table Builder</h2> 
            <img src = "templates/img/cars.png"/>
        </div>
        ''')
        html.write('{% endblock %}')

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
        html.write('<option value="" selected > -- select an option -- </option>')
        for e in categorical_elements:
            html.write("<option value='%s'>%s</option>\n"%(e,e))

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
                <select required class="selectpicker show-menu-arrow" name="col" id="col">
        ''')
        html.write('<option value="" selected > -- select an option -- </option>')
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
                <select class="selectpicker show-menu-arrow" name="val" id="val">
        ''')
        html.write('<option value="" selected > -- select an option -- </option>')
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
                    <option value="" selected > -- select an option -- </option>
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
                <div class="row"> <label for = "filter_label"> Category Filter </label> </div>
                <div class="row">
                    <select class="selectpicker show-menu-arrow" name="filter category" id="filter category">
        ''')
        html.write('<option value="" selected > -- select an option -- </option>')
        for e in filter_elements:
            html.write("<option value='%s'>%s</option>"%(e,e))

        html.write('''
                </select>
            </div>
        ''')

        # filter method
        html.write('''
            <div class="row"> 
                <select class="selectpicker show-menu-arrow" name="filter method" id="filter method">
                  <option value="" selected > -- select an option -- </option>
                  <option value="=">equal to</option>
                  <option value="!=">not equal to</option>
                  <option value=">">greater than</option>
                  <option value=">=">equal to or greater than</option>
                  <option value="<">less than</option>
                  <option value="<=">equal to or less than</option>
                </select>
            
        ''')

        #filter value
        html.write('''
                <div class="row">
                <input type="text" name = "filter value"/>
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

