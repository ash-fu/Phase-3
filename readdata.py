

import csv

content = open("data_2012.csv")
reader = csv.reader(content)
headers = reader.next()

print headers