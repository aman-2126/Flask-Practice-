import requests

Params = {"name": "aman", "post": "intern", "company": "amex"}
d = requests.get(url="http://127.0.0.1:5000/", json=Params)

data = d.json()
print(data)
