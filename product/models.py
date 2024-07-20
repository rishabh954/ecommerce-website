from django.db import models
from django.utils.safestring import mark_safe

# Create your models here.
class contactform(models.Model):
    name = models.CharField(max_length = 100)
    email = models.EmailField(max_length = 50)
    message = models.TextField()
    
    def __str__(self):
        return self.name

CATEGORY_CHOICES = (
    ('vg','vegitables'),
    ('ft','fruits'),
    ('bd','bread'),
    ('mt','meat'),
)

class product(models.Model):
    title = models.CharField(max_length = 100)
    name = models.CharField(max_length = 50)
    description = models.TextField()
    price = models.FloatField()
    category =models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    product_image = models.ImageField(upload_to= 'static/product_image')

    def __str__(self):
        return self.name
    
class user(models.Model):
    name = models.CharField(max_length=30)
    email_id = models.EmailField(null=True)
    mobile_no = models.IntegerField() #new field added
    # dob = models.DateField(null=True)
    # gender = models.CharField(choices=gender_list,max_length=6,null=True)
    city = models.CharField(max_length=30,null=True)
    propic = models.ImageField(upload_to='users',null=True,default='img/avatar.jpg')
    password = models.CharField(max_length=15)


    def __str__(self):
        return self.name

    def user_photo(self):
        return mark_safe('<img src="{}" width="100px" height="100px"/>'.format(self.propic.url))