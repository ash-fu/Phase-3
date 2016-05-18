# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np

df = pd.read_csv("data_2012.csv")
df.head()

agg = []

#example print table = constructPT(data,"Date (Intervals)","Sex of Casualty","Number of Vehicles","sum")
#print table.to_html()
def constructPT(dataset,rows,columns,values,agg):
    
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