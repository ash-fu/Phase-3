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
sepal_length = {}
sepal_width = {}

for row in data:
    # Iris-setosa, Iris-versicolour, or Iris-virginica
    species = row[4]
    if species not in petal_length:
        petal_length[species] = []
        petal_width[species] = []
        sepal_length[species] = []
        sepal_width[species] = []
    # first column contains sepal length
    sepal_length[species].append( float(row[0]) ) 
    # second column contains sepal width
    sepal_width[species].append( float(row[1]) ) 
    # third column contains petal length
    petal_length[species].append( float(row[2]) ) 
    # fourth column contains petal width
    petal_width[species].append( float(row[3]) ) 

clf()
subplot(221)
for species in petal_length:
    plot( petal_length[species], petal_width[species], "o" )
ylabel("petal width")

subplot(222)
for species in petal_length:
    plot( sepal_length[species], petal_width[species], "o" )

subplot(223)
for species in petal_length:
    plot( petal_length[species], sepal_width[species], "o" )
xlabel("petal length")
ylabel("sepal width")

subplot(224)
for species in petal_length:
    plot( sepal_length[species], sepal_width[species], "o" )
xlabel("sepal length")

all_species = petal_length
legend(all_species,loc='lower right', numpoints=1)    
webshow("iris_subplot.png")
