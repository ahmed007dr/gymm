from django.db import models
# from django.contrib.auth.models import User
# Create your models here.
FLAG_TYPE=(
    ('SOHAG','SOHAG'),
    ('AKHMEM','AKHMEM'),
    ('GIRGA','GIRGA'),
    ('RED-SEA','RED-SEA'),
                        )

class Product(models.Model):
    name = models.CharField(max_length=120)
    flag = models.CharField(max_length=20,choices=FLAG_TYPE)
    price = models.FloatField()
    image = models.ImageField(upload_to='product')
    sku = models.IntegerField()
    subtitle = models.TextField(max_length=400)
    discription = models.TextField(max_length=2000)
    brand = models.ForeignKey('Brand', related_name='product_brand', on_delete=models.CASCADE , null=True)
    

class ProductsImages(models.Model):
    product = models.ForeignKey(Product,related_name='product_images',on_delete=models.CASCADE)
    image = models.ImageField(upload_to='productsimages')

class Brand(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='brand')
