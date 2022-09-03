from django.urls import path


from . import views


urlpatterns= [
    path('',views.getAllProducts),
    path('get-user/<int:id>',views.getUserData),
    path('register-user',views.userRegister),
    path('login-user',views.login),
    path('get-all-products',views.getAllProducts),
    path('get-product-with-id/<int:product_id>',views.getProductWithId),
    path('get-product-with-user-id/<int:user_id>',views.getProductWithUserId),
    
]
