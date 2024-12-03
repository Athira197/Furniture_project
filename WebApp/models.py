from django.db import models
class ContactDb(models.Model):
    FirstName=models.CharField(max_length=50,null=True,blank=True)
    LastName=models.CharField(max_length=50,null=True,blank=True)
    Mobile=models.IntegerField(null=True,blank=True)
    Email=models.EmailField(max_length=50,null=True,blank=True)
    Message=models.TextField(max_length=50,null=True,blank=True)
class Registerdb(models.Model):
    Name = models.CharField(max_length=50,null=True,blank=True)
    Email = models.EmailField(max_length=50,null=True,blank=True)
    Mobile = models.IntegerField(null=True,blank=True)
    Password = models.CharField(max_length=50,null=True,blank=True)
    ConformPassword = models.CharField(max_length=50,null=True,blank=True)
class CartDb(models.Model):
    Name = models.CharField(max_length=50,null=True,blank=True)
    Product_Name = models.CharField(max_length=50,null=True,blank=True)
    Quantity = models.IntegerField(null=True,blank=True)
    Price = models.IntegerField(null=True,blank=True)
    Total_price = models.IntegerField(null=True,blank=True)
    Prod_Image=models.ImageField(upload_to="Cart Images",null=True,blank=True)
class OrderDb(models.Model):
    Name = models.CharField(max_length=100,null=True,blank=True)
    Email=models.EmailField(max_length=100,null=True,blank=True)
    Place=models.CharField(max_length=100,null=True,blank=True)
    Mobile=models.IntegerField(null=True,blank=True)
    Address=models.TextField(max_length=100,null=True,blank=True)
    State=models.CharField(max_length=100,null=True,blank=True)
    Pin=models.IntegerField(null=True,blank=True)
    TotalPrice=models.IntegerField(null=True,blank=True)
    Message=models.CharField(max_length=100,null=True,blank=True)





# Create your models here.
