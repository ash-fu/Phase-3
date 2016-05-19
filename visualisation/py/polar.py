import matplotlib
matplotlib.use('Agg')
from pylab import *

def webshow( img ):
    savefig( img, dpi=50 )
    print 'Content-Type: text/html\n'
    print '<img width="400" height="300" src="'+img+'" />'
	
clf()
# print Rose
a = 8.0 # try (a,b) = (8,5) (8,7)
b = 5.0
theta = arange(0.0, 2*b*pi, 0.02)
r = cos(a/b*theta)
subplot(111, polar=True)
plot(theta, r, "r-")
webshow("polar.png")
