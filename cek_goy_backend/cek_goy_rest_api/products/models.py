from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django.db.models.signals import post_save

class UserProfile(models.Model):
    one = '1'
    two = '2'
    three = "3"
    four = '4'
    five = "5"
    Rate = ((one,'1'),(two,"2"),(three,"3"),(four,"4"),(five,"5"))
    user= models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    rate = models.CharField(max_length=6,default=3,verbose_name='Rate',choices=Rate,blank=True)
    created_date = models.DateTimeField(auto_now_add=True)



class Category(models.Model):
    name = models.CharField(max_length=120)

    
class Product(models.Model):
    user  = models.ForeignKey("auth.User",on_delete = models.CASCADE)
    category = models.ManyToManyField(Category)
    title = models.CharField(max_length=120)
    content = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=15,decimal_places=2, default=99.99)
    created_date = models.DateTimeField(auto_now_add=True)
    productImage = models.FileField(blank=True, null=True, verbose_name="Product Image")
    
def create_profile(sender,**kwargs):
    if kwargs['created']:
        profile = UserProfile.objects.create(
            user = kwargs['instance']
        )
    
post_save.connect(create_profile,sender=User)
