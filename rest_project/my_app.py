import json
import requests

URL = 'http://localhost:9089/stu_info/3'

r = requests.get(url=URL)
print(type(r))
data = r.json()
print(type(data))

print(data)
