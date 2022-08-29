
import requests


endpoint = "http://127.0.0.1:8000/api"
endpoint1 = "http://127.0.0.1:8000/api/get-user/2"
getResponse = requests.get(endpoint)
getResponseUser = requests.get(endpoint1)
#print(getResponse.headers)
#print(getResponse.text)
#print(getResponse.status_code)
print(getResponse.json())
print(getResponseUser.json())
