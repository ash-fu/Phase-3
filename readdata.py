import csv

def getheaders(filename):
    content = open(filename)
    reader = csv.reader(content)
    headers = reader.next()
    data = zip(*reader)
    categorical_headers= []
    numerical_headers= []
    header_type = []
    count= 0
    for column in data:
        if column[1].isdigit():
            numerical_headers.append(headers[count])
        else:
            categorical_headers.append(headers[count])
        count +=1
    header_type.append(numerical_headers)
    header_type.append(categorical_headers)
    return header_type

def num_header(filename):
    headers = getheaders(filename)
    return headers[0]

def cate_header(filename):
    headers = getheaders(filename)
    return headers[1]

def gender(filename):
    content = open(filename)
    reader = csv.reader(content)
    headers = reader.next()
    male = []
    female = []
    for row in reader:
        if row[9] == "Male":
            male.append(row[10])
        else:
            female.append(row[10])
    return (male,female)
