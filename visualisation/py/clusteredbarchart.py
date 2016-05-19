import matplotlib
matplotlib.use('Agg')
from pylab import *
import calendar

def webshow(img):
    savefig(img,dpi=50)
    print 'Content-Type: text/html\n'
    print '<img width="400" height="300" src="'+img+'" />'
    
countries=['Afghanistan','Albania','Algeria','Angola']
births=[1143717,53367,598519,498887]
deaths=[529623,16474,144694,285380]
clf()
bar(arange(len(births))-0.3,births, width=0.3)
bar(arange(len(deaths)),deaths, width=0.3,color='r')
xticks( arange(len(countries)),countries, rotation=30)
webshow("clusteredbarchart.png")