import matplotlib
matplotlib.use('Agg')
from pylab import *
import urllib

def webshow( img ):
    savefig( img, dpi=50 )
    print 'Content-Type: text/html\n'
    print '<img width="400" height="300" src="'+img+'" />'

# Read the text of the first paragraph of Moby Dick
f = "http://ivle.informatics.unimelb.edu.au"
f += "/media/subjects/600151/exercise_data/moby.txt"
moby = urllib.urlopen(f)
text = moby.read()
tally = zeros(26) # initialize frequencies of 26 characters
charset = [chr(i) for i in arange(65,65+26)] # 'A'-'Z'
for char in text:
    ch = char.upper()
    if ch in charset:
        tally[ord(ch)-65] += 1

clf()
barh(arange(26),tally,color=(0.3,0.4,0.4),linewidth=0)
yticks( arange(26),charset)
ylim(0,26)
webshow("moby.png")
