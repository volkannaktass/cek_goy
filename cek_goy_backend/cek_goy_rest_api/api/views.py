from django.shortcuts import render
from django.http import JsonResponse,HttpRequest,HttpResponse
from products.models import Product
import json
from django.contrib.auth.models import User
from products.forms import RegisterForm
#from django.forms.models import model_to_dict
from rest_framework.response import Response
from rest_framework.decorators import api_view
import requests
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate


@api_view(["GET","POST"])
def getAllProducts(request,*args,**kwargs):
    model_data = Product.objects.all().order_by("?").first()
    data = {}
    if model_data:
        #data = model_to_dict(model_data)
        data['id'] = model_data.id
        data['user'] = model_data.user.username
        data['category'] = model_data.category.name
        data['title'] = model_data.title
        data['content']= model_data.content
        data['price'] = model_data.price
        data['created_date'] = model_data.created_date
        data['productImage'] = model_data.productImage.url
    return Response(data)

@api_view(["GET","POST"])
def getProductWithId(request,product_id):
    model_data = Product.objects.get(id=product_id)
    print(model_data)
    data = {}
    if model_data:
        
        data['id'] = model_data.id
        data['user'] = model_data.user.username
        data['category'] = model_data.category.name
        data['title'] = model_data.title
        data['content']= model_data.content
        data['price'] = model_data.price
        data['created_date'] = model_data.created_date
        data['productImage'] = model_data.productImage.url
    return Response(data)


@api_view(["GET","POST"])
def getProductWithUserId(request,user_id):
    model_data = Product.objects.filter(user_id=user_id)
    print(model_data)
    dataList = []
    if model_data:
        for i in model_data:
            data = {}
            data['id'] = i.id
            data['user'] = i.user.username
            data['category'] = i.category.name
            data['title'] = i.title
            data['content']= i.content
            data['price'] = i.price
            data['created_date'] = i.created_date
            data['productImage'] = i.productImage.url
            dataList.append(data)
    print(dataList)
    return Response(dataList)








@api_view(["GET","POST"])
def getUserData(request,id):
    model_data = User.objects.get(id=id)
    data = {}

    if model_data:
        data['username'] = model_data.username
        data['email'] = model_data.email
        #data['firstname'] = model_data.firstname
        #data['lastname'] = model_data.lastname
    return Response(data)


@api_view(["POST"])
def userRegister(request):
    if request.method == 'POST':
        #print(json.loads(request.body))
        #print(request.body)
        
        #return Response("")

        data = json.loads(request.body)
        username = data["userName"]
        firstName = data["name"]
        lastName = data["lastName"]
        email = data["email"]
        password = data["password"]
        passwordConfirm = data["passwordConfirm"]
        print(email)
        print(password)
        userCheck = User.objects.filter(username = username)
        if userCheck:
            raise ValidationError(
                "Already Taken"
            )
        if password != passwordConfirm:
            raise ValidationError(
                'Password Error'
            )
        newUser = User(username=username,email=email,password=password)
        newUser.first_name = firstName
        newUser.last_name = lastName
        newUser.save()
        print(newUser.id)
        data = {
            'username':username,
            'email':email
        }
        return Response("")
    else:
        return 500

    
@api_view(["GET","POST"])
def login(request):
    
    data = json.loads(request.body)
    username = data["username"]
    password = data["password"]
    responseData = {}
    user = authenticate(username = username,password = password)
    if user is None:
        raise ValidationError("Username or Password is Incorrect")
    else:
        return Response("")




