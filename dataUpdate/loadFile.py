import simplejson

with open('items.json', 'r') as data_file:
    json_data = data_file.read()
dataList = simplejson.loads(json_data)
for data in dataList:
    print data["appID"]
