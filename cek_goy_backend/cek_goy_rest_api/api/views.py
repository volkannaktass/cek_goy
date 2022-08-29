from django.shortcuts import render
from django.http import JsonResponse,HttpRequest,HttpResponse
from products.models import Product
import json
from django.contrib.auth.models import User
from products.forms import RegisterForm
#from django.forms.models import model_to_dict


def api_home(request,*args,**kwargs):
    model_data = Product.objects.all().order_by("?").first()
    data = {}
    if model_data:
        #data = model_to_dict(model_data)
        data['id'] = model_data.id
        data['user'] = model_data.user.username
        data['title'] = model_data.title
        data['content']= model_data.content
        data['price'] = model_data.price
    return JsonResponse(data)
    #return HttpResponse(data, headers={"content-type": "application/json"})



def getUserData(request,id):
    model_data = User.objects.get(id=id)
    data = {}

    if model_data:
        data['username'] = model_data.username
        data['email'] = model_data.email
        #data['firstname'] = model_data.firstname
        #data['lastname'] = model_data.lastname
    return JsonResponse(data)
    
def userRegister(request):
    form = RegisterForm(request.POST or None)

    if form.is_valid():
        first_name = form.cleaned_data.get("first_name")
        print(first_name)
        last_name = form.cleaned_data.get("last_name")
        print(last_name)
        username = form.cleaned_data.get("username")
        print(username)
        password = form.cleaned_data.get("password")
        print(password)
        email = form.cleaned_data.get("email")
        print(email)
        user = User.objects.create_user(username,email,password)
        user.first_name = first_name
        user.last_name = last_name
        user.save()
        print(user)

        messages.info(request,"Registration Successful...")

        return redirect("index")
    context = {
            "form" : form,
            "profile_form" : profile_form,
        }
    return render(request,"register.html",context)
    
