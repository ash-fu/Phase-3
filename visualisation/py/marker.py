import matplotlib
matplotlib.use('Agg')
from pylab import *

def webshow( img ):
    savefig( img, dpi=50 )
    print 'Content-Type: text/html\n'
    print '<img web width="400" height="300" src="'+img+'" />'
	
clf()
t = arange(0.0, 2.05, 0.05)

# method 1: keyword arguments
plot( t, sin(t*10), 'k-', linewidth=3.0)
# plot a solid black line with thickness=3

# method 2: setp command
lines = plot(t, [4 for i in t], t, 4*t)
setp(lines, 'color', 'r' )
setp(lines, 'linestyle', ':' )
# plot two red dotted lines

# method 3: setp command
line1,line2 = plot(t, t**2, t, exp(t))
line1.set_marker('s')
line1.set_color('g')
line2.set_marker('^')
line2.set_color('b')
# plot two lines
# first line is drawn with green square marker
# second line is drawn with blue triangle marker

webshow("marker.png")
