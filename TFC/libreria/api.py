from sqlite3.dbapi2 import apilevel
import requests
import json

api_url = 'https://api.github.com/users/Jemena'

response = requests.get(api_url)
response.json()

print(response)