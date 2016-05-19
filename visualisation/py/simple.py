import matplotlib
matplotlib.use('Agg')
from pylab import *

clf() # clear the figure
plot([1,1,2,3,5,8,13]) # a plot of fibonacci sequence
savefig( "simple.png", dpi=50 ) # save to a PNG file
# generate HTML to display the image
print 'Content-Type: text/html\n'
print '<html><body>'
print '<p>My first matplotlib plot!</p>'
print '<img width="400" height="300" src="simple.png" />'
print '</body></html>'
