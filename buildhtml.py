import readdata

 
def dropdown(filename):
    html = "<!DOCTYPE html><html><body>"
    headers = readdata.cate_header(filename)
    #headers = readdata.cate_headers("data_2012.csv")
    html += "<select>"
    for header in headers:
        html += "<option value = '" + header + "'>" + header + "</option>"
    html += "</select></body></html>"
 
    return html
 
print dropdown("data_2012.csv")
