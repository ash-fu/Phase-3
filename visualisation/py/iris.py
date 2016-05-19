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
# use dictionary for keeping the list
# petal_length['Iris-setosa'] contains a list of measurements
# petal_length['Iris-setosa'] = [4.0 4.0 3.0 etc] 
petal_length = {} 
petal_width = {}


for row in data:
    # 3 species:
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
for species in petal_length: # for all 3 species
    # call plot function to generate scatter plot
    # use "o" argument to generate circle marker
    plot( petal_length[species], petal_width[species], "o" )

all_species = petal_length
legend(all_species,loc='lower right', numpoints=1)    
ylabel("petal width")
xlabel("petal length")

webshow("iris.png")
