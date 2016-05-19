# -*- coding: utf-8 -*-
import pandas as pd

data = pd.read_csv("data_2012.csv")
data.head()

def constructPT(data,rows,columns,values,agg):
    table = pd.pivot_table(data,index=rows,columns=columns,values=values,\
    aggfunc=agg,fill_value=0)
    return table
    
    