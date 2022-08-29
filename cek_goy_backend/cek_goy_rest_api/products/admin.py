from django.contrib import admin
from django.contrib.auth.models import User
from .models import UserProfile,Product,Category
# Register your models here.
@admin.register(UserProfile)
class UserProfile(admin.ModelAdmin):
    
    list_display = ["user","rate"]
    list_display_links = ["user","rate"]
    search_fields = ["user"]
    list_filter = ["created_date"]
    #actions = [copy]
    class Meta:
        model = UserProfile

@admin.register(Category)
class Category(admin.ModelAdmin):
    
    list_display = ["name"]
    list_display_links = ["name"]
    search_fields = ["name"]
    list_filter = ["name"]
    #actions = [copy]
    class Meta:
        model = Category

        


@admin.register(Product)
class Product(admin.ModelAdmin):
    
    list_display = ["user","title","content","price","productImage"]
    list_display_links = ["user","title","content","price","productImage"]
    search_fields = ["user","title","content"]
    list_filter = ["created_date"]
    #actions = [copy]
    class Meta:
        model = Product

        
