import matplotlib
#matplotlib.use('Agg')
from pylab import *
import urllib
import csv

def webshow( img ):
    savefig( img, dpi=72 )
    print 'Content-Type: text/html\n'
    print '<img web width="400" height="300" src="'+img+'" />'

webdata = urllib.urlopen("http://ivle.informatics.unimelb.edu.au/media/subjects/600151/exercise_data/max_temp.csv","r")
data = csv.reader(webdata)
header = data.next()[1:]
data2 = list(data)
cities = [data2[i][0] for i in range(len(data2)) ]

figure(figsize=(10,4),dpi=72)

clf()
for line in data2:
    plot (line[1:], linewidth=2) 
    
legend(cities, loc='lower right', numpoints=40,
    prop=matplotlib.font_manager.FontProperties(size='smaller'))
xticks( arange(len(header)), header )
ylim(12,45)
xlim(-1,15)
ylabel("in degree Celcius")
grid(False)
axes().xaxis.grid(True, color=(0.8,0.8,0.8), linestyle="-", which='major')
title("Average Maximum Temperature of Australian Cities (Mar 2007 to Feb 2008)")
#show()
webshow("maxtemp.png")
