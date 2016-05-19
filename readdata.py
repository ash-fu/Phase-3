import csv


content = open("data_2012.csv")
reader = csv.reader(content)
headers = reader.next()
data = zip(*reader)

categorical_headers= []
numerical_headers= []

count= 0
for column in data:
        if column[1].isdigit():
            numerical_headers.append(headers[count])
        else:
            categorical_headers.append(headers[count])
        count +=1

print categorical_headers
    
