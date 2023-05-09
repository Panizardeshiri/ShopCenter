from django.db import models
from django.utils.text import slugify

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(blank=True,null=True)

    def save(self):
        self.slug = slugify(self.title)

        super(Category, self).save()


    def __str__(self):
        return self.slug



class Product(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(blank=True,null=True)
    price=models.IntegerField(null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    add_to_favorite = models.BooleanField(default=False)
    barnd = models.TextField(blank=True,null=True)
    size = models.TextField(blank=True,null=True, default=1)
    color = models.TextField(blank=True,null=True) 
    exist = models.BooleanField(default=False)
    price_off = models.IntegerField()



    def total_price(self):

        total_price = self.price - self.price*self.price_off*0.01

        return total_price
    

    def __str__(self):
        return self.name
    
   



