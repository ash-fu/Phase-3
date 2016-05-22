# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np

dataset = pd.read_csv("data_2012.csv")
dataset.head()


#example print table = constructPT("Date (Intervals)","Sex of Casualty","Number of Vehicles","sum")
#print table.to_html()

def filterData():
    dataset = pd.read_csv("leeds-2012.csv")
    return dataset.loc[(dataset["Age of Casualty"] > 16), ["Sex of Casualty","Road Surface", "Casualty Class","Age of Casualty"]]

def constructPT(rows,columns,values,agg):
    
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
    
    table = pd.pivot_table(dataset,index=rows,columns=columns,values=values,\
    aggfunc=agg_action,fill_value=0,margins=True,dropna=True)
    return table
    
def filterPT(table,attribute,filterValue):
    table = table.query('%s == ["%s"]' % (attribute, filterValue))
    return table

# simulation
data = filterData()
table = constructPT(data, "Road Surface", "Casualty Class","Age of Casualty","minimum")
print table