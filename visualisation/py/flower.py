import matplotlib
matplotlib.use('Agg')
from pylab import *

def webshow( img ):
    savefig( img, dpi=50 )
    print 'Content-Type: text/html\n'
    print '<img width="400" height="300" src="'+img+'" />'

clf()
# draw epicycloid
a = 10.0 # try (a,b) = (10,7) (2,7) (4,7) (5,3)
b = 7.0 
t = arange (0.0, 2*a*pi, 0.1)
x = (1 + a/b)*cos(t) - (a/b)*cos((b/a + 1)*t)
y = (1 + a/b)*sin(t) - (a/b)*sin((b/a + 1)*t)
plot(x,y,'',linewidth=1, antialiased=True)
axis('off')
axis('equal')
webshow("flower.png")