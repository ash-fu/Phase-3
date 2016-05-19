import matplotlib
matplotlib.use('Agg')
from pylab import *
import calendar

def webshow(img):
    savefig(img,dpi=50)
    print 'Content-Type: text/html\n'
    print '<img width="400" height="300" src="'+img+'" />'
	
clf()
t = arange(0.0, 2.05, 0.05)
plot(t, t**2, t, exp(t))
legend(["square","e"],loc='lower right')
ylabel("ft",fontsize=10)
xlabel("t",fontsize=10)

webshow("legend.png")


