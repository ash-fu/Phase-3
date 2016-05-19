import matplotlib
matplotlib.use('Agg')
from pylab import *

def webshow( img ):
    savefig( img, dpi=50 )
    print 'Content-Type: text/html\n'
    print '<img width="400" height="300" src="'+img+'" />'

clf()
world=["USA","China","Russia","India","Japan","Germany","Canada","UK","Others"]
co2=[20.90,17.30,5.30,4.60,4.30,2.80,2.20,2.00,40.60]
colors=['b','g','r','c','m','y','k','w','#cccccc' ]
pie(co2,explode=None,labels=world,colors=colors)
axis('equal')
webshow("pie.png")