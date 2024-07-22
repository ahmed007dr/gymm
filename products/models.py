from django.db import models
from django.utils.text import slugify

# from django.contrib.auth.models import User
# Create your models here.
FLAG_TYPE=(
    ('SOHAG','SOHAG'),
    ('AKHMEM','AKHMEM'),
    ('GIRGA','GIRGA'),
    ('RED-SEA','RED-SEA'),
                        )

class Gym(models.Model):
    name = models.CharField(max_length=120)
    flag = models.CharField(max_length=20,choices=FLAG_TYPE)
    price = models.FloatField()
    image = models.ImageField(upload_to='gym')
    sku = models.IntegerField()
    subtitle = models.TextField(max_length=400)
    discription = models.TextField(max_length=2000)
    brand = models.ForeignKey('Brand', related_name='gym_brand', on_delete=models.CASCADE , null=True)
    slug = models.SlugField(blank=True,null=True)

    def save(self, *args, **kwargs):
       self.slug = slugify(self.name)
       super(Gym, self).save(*args, **kwargs) 

    def __str__(self):
        return self.name
    
    

class GymImages(models.Model):
    product = models.ForeignKey(Gym,related_name='gym_images',on_delete=models.CASCADE)
    image = models.ImageField(upload_to='gymimages')

class Brand(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='brand')
    def save(self, *args, **kwargs):
       self.slug = slugify(self.name)
       super(Gym, self).save(*args, **kwargs) 

    def __str__(self):
        return self.name
    
    