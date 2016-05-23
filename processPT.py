# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import csv

dataset = pd.read_csv("data_2012.csv")
dataset.head()
content = open("data_2012.csv")
reader = csv.reader(content)
header = reader.next();

#example print table = constructPT(data,"Date (Intervals)","Sex of Casualty","Number of Vehicles","sum")
#print table.to_html()


def filterData(element,userInput,filterMethod):
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
    aggfunc=agg_action,fill_value=0,margins=True,dropna=True)
    table.columns = table.columns.droplevel(0)
    return table

# simulation
# data = filterData()
# table = constructPT(data,"Road Surface", "Casualty Class","Age of Casualty","minimum")
# print table