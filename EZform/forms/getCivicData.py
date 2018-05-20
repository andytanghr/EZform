from urllib import request
import json

url = 'https://www.googleapis.com/civicinfo/v2/elections?key=AIzaSyAkjEEFiNGqMzzSKWNJ4HbvkGCXlLakzIM'
serialized_data = request.urlopen(url).read()
#
data = json.loads(serialized_data)
#
print(data)




 https://www.googleapis.com/civicinfo/v2/voterinfo?key=AIzaSyAkjEEFiNGqMzzSKWNJ4HbvkGCXlLakzIM&address=8502+Star+Hollow+Ln,+Houston,+TX&electionid=4454&returnAllAvailableData=true
