import matplotlib
matplotlib.use('Agg')
from pylab import *

clf()
plot([1,2,3,4])
savefig('first.png',dpi=50)

clf()
plot([1,2,3,4], [1,4,9,16], 'ro')
axis([0, 6, 0, 20])
savefig('second.png',dpi=50)

print 'Content-Type: text/html\n'
print '<img webshow width="400" height="300" src="first.png" /><br />'
print '<img webshow width="400" height="300" src="second.png" />'
