from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _



FLAG_TYPE=(
    ('SOHAG','SOHAG'),
    ('AKHMEM','AKHMEM'),
    ('GIRGA','GIRGA'),
    ('RED-SEA','RED-SEA'),
                        )

class Gym(models.Model):
    name = models.CharField(max_length=120,verbose_name=_('name'))
    flag = models.CharField(_('flag'),max_length=20,choices=FLAG_TYPE)
    price = models.FloatField(_('price'))
    image = models.ImageField(_('image'),upload_to='gym')
    sku = models.IntegerField()
    subtitle = models.TextField(_('subtitle'),max_length=400)
    discription = models.TextField(_('discription'),max_length=2000)
    brand = models.ForeignKey('Brand', verbose_name=_('brand'),related_name='gym_brand', on_delete=models.CASCADE , null=True)
    slug = models.SlugField(blank=True,null=True,unique=True)

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
       super(Brand, self).save(*args, **kwargs) 

    def __str__(self):
        return self.name
    
    