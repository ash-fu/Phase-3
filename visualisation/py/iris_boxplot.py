import matplotlib
matplotlib.use('Agg')
from pylab import *
import urllib
import csv

def webshow( img ):
    savefig( img, dpi=50 )
    print 'Content-Type: text/html\n'
    print '<img width="400" height="300" src="'+img+'" />'

f = "http://ivle.informatics.unimelb.edu.au/"
f += "media/subjects/600151/exercise_data/iris.csv"
webdata = urllib.urlopen(f,"r")
data = list(csv.reader(webdata))
petal_length = {}
petal_width = {}

for row in data:
    # Iris-setosa, Iris-versicolour, or Iris-virginica
    species = row[4]
    if species not in petal_length:
        petal_length[species] = []
        petal_width[species] = []	
    # third column contains petal length
    petal_length[species].append( float(row[2]) ) 
    # fourth column contains petal width
    petal_width[species].append( float(row[3]) ) 

clf()
# boxplot two variables:
# Iris-setosa's petal_width and Iris-virginica's petal_width
boxplot( [petal_width['Iris-setosa'], petal_width['Iris-virginica']] )
ylim(0,3)
xticks( arange(3), ['','Iris-setosa','Iris-virginica'] )
ylabel( "petal width" )
webshow("iris_boxplot.png")
