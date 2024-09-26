import requests

#---allocate url
# https://jsonplaceholder.typicode.com/users

URL = "http://127.0.0.1:8000/apiinfo/"

#-----get url data
response = requests.get(url=URL)
#---extract into json
data = response.json()
print(data)