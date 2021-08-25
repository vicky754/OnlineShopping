from django.db import models

class product(models.Model):
    name=models.CharField(max_length=50)
    discription=models.CharField(max_length=500 )
    price=models.IntegerField(default=0)
    active = models.BooleanField(default=True)
    discount=models.IntegerField(default=0)
    file = models.FileField(upload_to='uploads/files',blank=True)
    thumbnil=models.ImageField(upload_to="uploads/thumbnils")
    link=models.CharField(null=True,blank=True,max_length=200)
    fileSize=models.CharField(null=True,max_length=10)
    Quantity=models.IntegerField(default=1)

class ProductImages(models.Model):
    product=models.ForeignKey(product,default=None,on_delete=models.CASCADE)
    image=models.ImageField(upload_to="uploads/images",blank=True)


class user(models.Model):
    name=models.CharField(max_length=50)
    active = models.BooleanField(default=True)
    email=models.CharField(max_length=100)
    password=models.CharField(max_length=500)
    phone=models.CharField(max_length=10)
    