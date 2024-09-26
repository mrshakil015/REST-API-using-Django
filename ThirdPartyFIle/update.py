import requests
import json

URL = "http://127.0.0.1:8000/apiupdate/"

data = {
    'id': 9,
    'teacher_name': 'Tansen',
    'course_name': 'Machine Learning',

}

#-----Convert python data into json
json_data = json.dumps(data)
r = requests.put(url=URL, data=json_data)
data = r.json()
print(data)