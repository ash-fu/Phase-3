import pandas as pd
import numpy as np
import csv

#Contains all the different functions that help construct the pivot table
# and pivot table builder

FILENAME = "data_2012.csv"

#Gets the header of the csv file. Appends 2 lists into one header list. 
#The first list contains the numerical headers and second list contains all the categorical.
def getelements():
    content = open(FILENAME)
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

#Filters data according to the specified inputs
def filterData(element,userInput,filterMethod,headers):
    dataset = pd.read_csv(FILENAME)
    dataset.head()
    content = open(FILENAME)
    reader = csv.reader(content)
    header = reader.next();
    
    if(element== "No Filter"):
        filteredData = dataset
        return filteredData

    if(element in headers[0]):
        userInput = int(userInput)
        if (filterMethod == ">"):
            filteredData =  dataset.loc[(dataset[element] > userInput), header]
        elif (filterMethod == ">="):
            filteredData =  dataset.loc[(dataset[element] >= userInput), header]
        elif (filterMethod == "<"):
            filteredData =  dataset.loc[(dataset[element] < userInput), header]
        else:
            filteredData =  dataset.loc[(dataset[element] <= userInput), header]
            
    else: 
        if (filterMethod == "="):
            filteredData =  dataset.loc[(dataset[element] == userInput), header]
        else:
            filteredData =  dataset.loc[(dataset[element] != userInput), header]
    return filteredData
    
# Constructs a pivot table according to the row and col arguments as well as the 
# filtered data
def constructPT(data,rows,columns,values,agg):
    
    if(agg == "sum"):
        agg_action = [np.sum]
    elif(agg == "minimum"):
        agg_action = [np.min]
    elif(agg == "maximum"):
        agg_action = [np.max]
    elif(agg == "median"):
        agg_action = [np.median]
    else:
        agg_action = [np.mean]

    table = pd.pivot_table(data,index=rows,columns=columns,values=values,\
    aggfunc=agg_action,margins=True,fill_value=0,dropna=True)
    table.columns = table.columns.droplevel(0)
    return table

# Finds the correct colour for the table row
def getColoredRow(maxVal,val):
    if(isNum(val)!=True):
        return '<th>%s</th>\r'%(val)
    else:
        val = float(val)
        red = 255
        green = 150 - 150*val/maxVal
        blue = 100
        if (val==0):
            red=255
            green=255
            blue=255
        val = int(val)
        color = '<td style="background-color: rgb(%d,%d,%d)">%s</td>\r'%(red,green,blue,val)
        return color

# Checks if argument is a number or another type of variable
def isNum(s):
    try:
        float(s)
        return True
    except ValueError:
        return False