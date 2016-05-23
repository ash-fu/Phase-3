import pandas as pd
import numpy as np
import csv

dataset = pd.read_csv("data_2012.csv")
dataset.head()
content = open("data_2012.csv")
reader = csv.reader(content)
header = reader.next();

def filterData(element,userInput,filterMethod):
    if(element== "No Filter"):
        filteredData = dataset
        return filteredData
    if (filterMethod == ">"):
        filteredData =  dataset.loc[(dataset["%s"%(element)] > "%s"%(userInput)), header]
    elif (filterMethod == ">="):
        filteredData =  dataset.loc[(dataset["%s"%(element)] >= "%s"%(userInput)), header]
    elif (filterMethod == "<"):
        filteredData =  dataset.loc[(dataset["%s"%(element)] < "%s"%(userInput)), header]
    elif (filterMethod == "<="):
        filteredData =  dataset.loc[(dataset["%s"%(element)] <= "%s"%(userInput)), header]
    elif (filterMethod == "="):
        filteredData =  dataset.loc[(dataset["%s"%(element)] == "%s"%(userInput)), header]
    else:
        filteredData =  dataset.loc[(dataset["%s"%(element)] != "%s"%(userInput)), header]
    return filteredData
    

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
    aggfunc=agg_action,margins=True,dropna=True)
    table.columns = table.columns.droplevel(0)
    return table

def getColoredRow(maxVal,val):
    white = [255,255,255]
    orange = [255,63,0]
    red = white[ 0 ] + ((orange[0] - white[0] ) * val / maxVal )
    green = white[ 1 ] + ((orange[1] - white[1] ) * val / maxVal )
    blue = white[ 2 ] + ((orange[2] - white[2] ) * val / maxVal )
    
    color = '<td style="background-color: rgb(%s,%s,%s)">%s</td>;'%(red,green,blue,val)
    return color
    
#table.values.min()
#table.values.max()
#table.drop('All', axis=1)
#table.drop('All')