import csv

def getheaders(filename):
   content = open(filename)
   reader = csv.reader(content)
   headers = reader.next()
   return headers
