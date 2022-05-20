import requests

endpoint = "http://127.0.0.1:8000/"

data = requests.get(endpoint)
print("data:",data.json())