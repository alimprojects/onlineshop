# import the standard Django Model
# from built-in library
from django.db import models
from django.utils.html import mark_safe
  
# declare a new model with a name "GeeksModel"

class Member(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    joined_date = models.DateField()
    def __str__(self):
        return f"{self.firstname} {self.lastname}"

class Products (models.Model):
    product_name = models.CharField(max_length=200)
    product_description = models.TextField()
    supplier_id = models.IntegerField()
    category_id = models.IntegerField()
    unit = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=15, decimal_places=2)
    photo = models.ImageField(upload_to='images/products')

    def image_tag(self):
        return mark_safe('<img src="%s" width="100px" height="100px" />'%(self.photo.url))
    image_tag.short_description = 'Image'
    image_tag.allow_tags = True
    
class Categories (models.Model):
    category_name = models.CharField(max_length=200)
    description = models.TextField()
    
class Contacts (models.Model):
    contact_name = models.CharField(max_length=200)
    contact_email = models.EmailField(max_length=200)
    message = models.TextField()
    
class Reviews (models.Model):
    product_id = models.IntegerField()
    customer_name = models.CharField(max_length=200)
    customer_email = models.EmailField(max_length=200)
    review = models.TextField()
    rate = models.IntegerField()
    datetime = models.DateTimeField(auto_now_add=True)
