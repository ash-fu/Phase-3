import matplotlib
matplotlib.use('Agg')
from pylab import *
#from math import *

def webshow(img):
    savefig(img,dpi=50)
    print 'Content-Type: text/html\n'
    print '<img width="400" height="300" src="'+img+'" />'

def f(t):
    return cos(2*pi*t)*log(1+t)

precision = 0.1 # change to 0.02
t=arange(0.0, 5.0, precision)
clf()
plot(t,f(t),'k')	
webshow("simple2.png")
