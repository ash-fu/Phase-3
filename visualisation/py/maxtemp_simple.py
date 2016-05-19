import matplotlib
matplotlib.use('Agg')
from pylab import *
import urllib
import csv

def webshow( img ):
    savefig( img, dpi=50 )
    print 'Content-Type: text/html\n'
    print '<img width="400" size="300" src="'+img+'" />'

f = "http://ivle.informatics.unimelb.edu.au/"
f += "media/subjects/600151/exercise_data/max_temp.csv"
webdata = urllib.urlopen(f,"r")
data = list(csv.reader(webdata))
months = data[0][1:]
cities = [data[i][0] for i in range(len(data[1:])) ]

clf()
for line in data[1:]:
    plot (line[1:], linewidth=2) 
    
legend(cities, loc='lower right', numpoints=40,
    prop=matplotlib.font_manager.FontProperties(size='smaller'))
xticks( arange(len(months)), months )
ylim(12,45)
xlim(-1,15)
ylabel("in degree Celcius")
grid(False)
axes().xaxis.grid(True, color=(0.8,0.8,0.8), linestyle="-", which='major')
title("Average Maximum Temperature of Australian Cities (Mar 2007 to Feb 2008)")
webshow("maxtemp_simple.png")
