import matplotlib
matplotlib.use('Agg')
from pylab import *
from numpy import *
import urllib
import csv

def webshow( img ):
    savefig( img, dpi=50 )
    print 'Content-Type: text/html\n'
    print '<img width="400" height="300" src="'+img+'" />'

# data from Jan 1990 to Mar 2008
f = "http://ivle.informatics.unimelb.edu.au/"
f += "media/subjects/600151/exercise_data/au_int.csv"
webdata = urllib.urlopen(f,"r")
data = list(csv.reader(webdata))
hist_rates = [] # historical rates 
years = [] # ticks text for year
y_loc = [] # ticks location
prev_idx = 0 # index to previous month

for arow in data:
    rate = float(arow[1]) # interest rate
    date = arow[0].split('/') # data of interest rate change
    month = int(date[0])-1 # map jan-dec to 0-11
    year = int(date[2])-1990 # map 1990-2008 to 0-18 
    idx = year*12 + month
    for i in arange(prev_idx, idx+1): # filling earlier months
        hist_rates.append( rate ) # build hist_rates
        if i%12 == 0: # if january build years ticks
            y_loc.append( i )
            years.append( str(1990+year) )
    prev_idx = idx+1

clf()
plot(hist_rates)
xticks( y_loc,years,rotation='vertical' )
webshow("interest.png")
