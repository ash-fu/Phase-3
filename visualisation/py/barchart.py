import matplotlib
matplotlib.use('Agg')
from pylab import *
import calendar

def webshow(img):
    savefig(img,dpi=50)
    print 'Content-Type: text/html\n'
    print '<img width="400" height="300" src="'+img+'" />'
	
countries=['Burundi','Ethiopia','DRep of Congo','Switzerland','Norway','Luxembourg']
gnp=[90,110,110,49600,51810,56380] # GNP per capita (2004)
clf()
bar(arange(len(gnp)),gnp)
xticks( arange(len(countries)),countries, rotation=30)
webshow("barchart.png")
