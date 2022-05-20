import requests
import json
URL = "http://127.0.0.1:8000/create/stucreate/"
data = {
    'name': 'yyeeoo',
    'roll': 10,
    'city': 'aaa'
}
json_data = json.dumps(data)
req = requests.post(url=URL, data=json_data)
print(req.json())