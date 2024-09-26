import requests
import json

URL = "http://127.0.0.1:8000/apidelete/"

data = {
    'id' : 5,
}
#-----Convert python data into json
json_data = json.dumps(data)
r = requests.delete(url=URL, data = json_data)
#-----extract
data = r.json()
print(data)