from django.db import models
from django.contrib.auth.models import User
import datetime
import os

def getFilename(request, filename):
    now_time=datetime.datetime.now().strftime("%Y%m%d%H:%M:%S")
    new_filename="%s%s"%(now_time,filename)
    return os.path.join('upload/', new_filename)
class Catagory(models.Model):
    name = models.CharField(max_length=150, null=False, blank=False)
    Image = models.ImageField(upload_to=getFilename, null=False, blank=False)
    description = models.TextField(max_length=500,null=False, blank=False)
    status = models.BooleanField(default=False, help_text="0-show, 1-Hidden")
    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    catagory = models.ForeignKey(Catagory,on_delete=models.CASCADE)
    name = models.CharField(max_length=150, null=False, blank=False)
    quantity = models.IntegerField(null=False, blank=False)
    price = models.IntegerField(null=False, blank=False)
    prodect_Image = models.ImageField(upload_to=getFilename, null=False, blank=False)
    description = models.TextField(max_length=500,null=False, blank=False)
    status = models.BooleanField(default=False, help_text="0-shows, 1-Hidden")
    trending = models.BooleanField(default=False, help_text="0-default, 1-Trending")
    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    product_qty=models.IntegerField(null=False, blank=False)
    createdAt = models.DateTimeField(auto_now_add=True)

    @property
    def total_cost(self):
        return self.product_qty*self.product.price