import requests, json

URL = "http://127.0.0.1:8000/apicreate/"

data = {
    'teacher_name': 'Rohim',
    'course_name': 'Deep Learning',
    'course_duration': 3,
    'seat': 20,
}

json_data = json.dumps(data)
re = requests.post(url=URL, data = json_data)
data = re.json()
print(data)