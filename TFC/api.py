import json
import requests

with open('paint.json', 'r') as json_file:
    json_data = json.load(json_file)

api_url = 'https://api.github.com/users/Jemena'

response = requests.post('https://httpbin.org/post', json=json_data)
#response = requests.get('https://httpbin.org/post', json=json_data)
print("Status code: ", response.status_code)
print(response.json())


#No estoy seguro q nos exigen exactamente