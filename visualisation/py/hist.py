import matplotlib
matplotlib.use('Agg')
from pylab import *

def webshow( img ):
    savefig( img, dpi=50 )
    print 'Content-Type: text/html\n'
    print '<img width="400" height="300" src="'+img+'" />'

clf()
ages=[17,18,18,19,21,19,19,21,20,23,19,22,20,21,19,19,14,23,16,17 ]
hist(ages, bins=10)
grid(False)
axes().yaxis.grid(True, which='major')
webshow("hist.png")