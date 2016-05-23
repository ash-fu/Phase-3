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

            {% block content %}
            <form method="post" action="pivot_table">

            <!--Filter-->
              <p>Filter Category:
                <select name="Filter Category">
        ''')
        filter_elements=["No Filter"]+all_elements
        for e in filter_elements:
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
                  <option value="sum">Sum</option>
                  <option value="median">Median</option>
                  <option value="maximum">Maximum</option>
                  <option value="minimum">Minimum</option>
                  <option value="mean">Mean</option>
                </select>
              </p>
              <p>
                <input type="submit" />
              </p>
            </form>
            {% endblock %}
        ''')
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
