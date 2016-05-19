import matplotlib
matplotlib.use('Agg')
from pylab import *
import calendar

def webshow(img):
    savefig(img,dpi=50)
    print 'Content-Type: text/html\n'
    print '<img width="400" height="300" src="'+img+'" />'

# Melbourne temperature Mar 2007 - Feb 2008	
t=[41.2,35.5,37.4,29.3,23.9,16.8,18.2,25.7,22.3,33.5,36.9,41.1]
clf()
plot(t) 
# print 'jan' - 'dec'
xticks(arange(12),list(calendar.month_abbr)[1:])
webshow("maxmel.png")
