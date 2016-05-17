import readdata

 
def dropdown(filename):
    html = "<!DOCTYPE html><html><body>"
    headers = readdata.getheaders(filename)
 	#headers = readdata.getheaders("data_2012.csv")
    html += "<select>"
    for header in headers:
        html += "<option value = '" + header + "'>" + header + "</option>"
    html += "</select></body></html>"
 
       #print html
    return html
 

#==============================================================================
# html = "<!DOCTYPE html><html><body>"
# headers = readdata.getheaders("data_2012.csv")
# html += "<select>"
# for header in headers:
#     html += "<option value = '" + header + "'>" + header + "</option>" 	
# html += "</select></body></html>"
# 
# print html
#==============================================================================
#return html
