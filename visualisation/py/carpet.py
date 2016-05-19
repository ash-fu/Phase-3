import matplotlib
matplotlib.use('Agg')
from pylab import *

def webshow( img ):
    savefig( img, dpi=50 )
    print 'Content-Type: text/html\n'
    print '<img web width="400" height="300" src="'+img+'" />'

clf()
N = 3 # 3, 5, 7, 9, try odd numbers
w = 243
A = [[0] * w for i in range(w)]
I = A

#int first row and first column
for i in range(w):
    A[0][i] = 1
    A[i][0] = 1

for i in range(1,w):
    for j in range(1,w):
        A[i][j] = (A[i-1][j]+A[i][j-1]+A[i-1][j-1]) % N

for i in range(w):
    for j in range(w):
        if A[i][j] == 0: I[i][j] = 1
        else: I[i][j] = 0

imshow( I, cmap=cm.gray, interpolation='nearest' )
axis('off')

webshow("carpet.png")