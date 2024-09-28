import requests, json

URL = "https://userapi.rainbowitpoint.com/user-create/"

data = {
    'name': 'Rohim',
    'username': 'rohim01',
    'email': 'rohim123@gmail.com',
    'address': 'mirpur',
    'website': 'www.rohim.com',
    
}

json_data = json.dumps(data)
re = requests.post(url=URL, data = json_data)
data = re.json()
print(data)