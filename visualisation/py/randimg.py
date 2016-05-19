import matplotlib
matplotlib.use('Agg')
from pylab import *

def webshow( img ):
    savefig( img, dpi=50 )
    print 'Content-Type: text/html\n'
    print '<img web width="400" height="300" src="'+img+'" />'

clf()
x = rand(20,20)
imshow( x )
webshow("randimg.png")