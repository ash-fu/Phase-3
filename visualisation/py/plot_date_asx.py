import matplotlib
matplotlib.use('Agg')
from pylab import *
from datetime import date
import calendar,csv,urllib,sys

# creates a list of 'Jan'-'Dec'
threeLettersMonth = list(calendar.month_abbr)

# two data files
f = "http://ivle.informatics.unimelb.edu.au"
f += "/media/subjects/600151/exercise_data/"
buyDatesFile = f+"buy_dates.txt"
asx300File = f+"asx300.csv"

# function to produce a list from a CSV file
def getList(filename):
    webdata = urllib.urlopen(filename)
    data = list(csv.reader(webdata))
    return data

# function that reads file buy_dates.txt -------------------------
# format:
# 29 Jan 2008
# 23 Jan 2008

def readBuyDates():
    dateList = []    
    buyDateTable = getList(buyDatesFile)
    buyDateTable.reverse() # sort by date ascending
  
    for aRow in buyDateTable:
        fields = aRow[0].strip().split(" ") # get date from text 
        year = int(fields[2])
        month = threeLettersMonth.index(fields[1])
        day = int(fields[0])
        aBuyDate = date( year, month, day )
        dateList.append( aBuyDate )

    numDateList = [date2num(i) for i in dateList]
    return numDateList

# function that reads file asx300.csv ----------------------------
# format:
# Date,Open,High,Low,Close,Volume,Adj Close
# 22/02/2008,5589.6,5589.6,5498.7,5567.4,0,5567.4
# 21/02/2008,5504.6,5607.3,5504.6,5589.6,0,5589.6

def readAsxData():
    dateList = []
    closeList = []    
    asxDataTable = getList(asx300File)[1:]
    asxDataTable.reverse() # sort by date ascending
    
    for aRow in asxDataTable:
        closeValue = float(aRow[6])
        fields = aRow[0].strip().split("/") # get date from text 
        year = int(fields[2])
        month = int(fields[1])
        day = int(fields[0])
        aBuyDate = date( year, month, day )
        dateList.append( aBuyDate )    
        closeList.append( closeValue )

    numDateList = [date2num(i) for i in dateList]
    return (numDateList,closeList)
    
# main program
clf()
# 1. plot ASX 300 index from 2006-2008 --------------------------
(asxDateList,asxCloseList) = readAsxData()
plot_date(asxDateList, asxCloseList, 'b-')

# 2. plot only specific buy dates --------------------------------
buyDates = readBuyDates()
buyDateList = []
buyPriceList = []

for aBuyDate in buyDates: # for each buy date, find its price
    if aBuyDate in asxDateList:
        vIndex = asxDateList.index(aBuyDate)
        buyDateList.append( aBuyDate )
        buyPriceList.append(asxCloseList[vIndex])

plot_date(buyDateList, buyPriceList, 'rs', markersize=10)
# customize the output
xticks(rotation=-30, ha='left' )
grid(True)
savefig("plot_date_asx.png",dpi=50)
print 'Content-Type: text/html\n'
print '<img width="400" height="300" src="plot_date_asx.png" />'