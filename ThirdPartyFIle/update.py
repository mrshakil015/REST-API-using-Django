import requests
import json

URL = "http://127.0.0.1:8000/apiupdate/"

data = {
    'id': 3,
    'teacher_name': 'Tansen',
    'course_name': 'Machine Learning',

}

json_data = json.dumps(data)
r = requests.put(url=URL, data=json_data)
data = r.json()
print(data)