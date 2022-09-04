
import requests


data = {
    "userName":"berktest",
    "name":"berktest",
    "lastName":"karatastest",
    "email":"adas1313ad@afdsaf.com",
    "password":"Berk1234..",
    "passwordConfirm":"Berk1234.."
}



login = {
    "username": "berktest",
    "password": "Berk1234"
}

endpoint = "http://127.0.0.1:8000/api"
endpoint1 = "http://127.0.0.1:8000/api/get-user/2"
endpoint2 = "http://127.0.0.1:8000/api/register-user"
endpoint3 = "http://127.0.0.1:8000/api/login-user"
endpoint4 = "http://127.0.0.1:8000/api/get-all-products"
endpoint5 = "http://127.0.0.1:8000/api/get-product-with-id/2"
endpoint6 = "http://127.0.0.1:8000/api/get-product-with-user-id/5" 
#getResponse = requests.get(endpoint)
#getResponseUser = requests.get(endpoint1)
#getResponseUser = requests.get(endpoint2)
#getResponseProductWithId = requests.get(endpoint5)
getResponseProductWithUserId = requests.get(endpoint6)

#print(getResponseAllProducts.text)
#print(getResponseAllProducts.json())
#postRegisterUser = requests.post(endpoint2,json = data)
#postLoginUser = requests.post(endpoint3,json = login)
#print(postRegisterUser.text)
#print(getResponse.headers)
#print(getResponse.text)
#print(getResponse.status_code)
#print(getResponse.json())
#print(getResponseProductWithId.json())
print(getResponseProductWithUserId.json())
#print(getResponseUser.json())
