from django.db import models

# Create your models here.
from django.db import models
from django.urls import reverse

PRODUCT_TYPES = (
    ("1", 'Bakery'),
    ("2", 'Mexican food'),
    ("3", 'Fastfood'),
    ("4", 'Pizza'),
    ("5", 'Salad'),
    ("6", 'Traditional food'),
)
# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255, null=True)
    image = models.ImageField(upload_to='static/media/images',null=True)
    price = models.DecimalField(decimal_places=2, max_digits=6, null=True)
    quantity = models.IntegerField(null=True)
    description = models.TextField(null=True)
    type_prod = models.CharField(choices=PRODUCT_TYPES, max_length=30, null=True)
    um = models.CharField(max_length=10, null=True)

    def __str__(self):
        return self.name

