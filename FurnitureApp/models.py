from django.db import models
class FurnitureDb(models.Model):
    Category = models.CharField(max_length=50,null=True,blank=True)
    Description = models.TextField(max_length=50,null=True,blank=True)
    Image = models.ImageField(upload_to="cat_img",null=True,blank=True)
class ProductDb(models.Model):
    Product_Category = models.CharField(max_length=50,null=True,blank=True)
    Product_Name = models.CharField(max_length=50, null=True, blank=True)
    Quantity = models.IntegerField(null=True, blank=True)
    MRP = models.IntegerField(null=True,blank=True)
    Description = models.TextField(max_length=150, null=True, blank=True)
    Origin = models.CharField(max_length=50, null=True, blank=True)
    Manufacture = models.CharField(max_length=50, null=True, blank=True)
    Image1 = models.ImageField(upload_to="pro_image",null=True,blank=True)
    Image2 = models.ImageField(upload_to="pro_image", null=True, blank=True)
    Image3 = models.ImageField(upload_to="pro_image", null=True, blank=True)
class BlogDb(models.Model):
    Heading = models.CharField(max_length=50,null=True,blank=True)
    BImage = models.ImageField(upload_to="blog_img",null=True,blank=True)

# Create your models here.
