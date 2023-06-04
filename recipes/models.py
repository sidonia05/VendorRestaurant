
from django.db import models
# Create your models here.
class Recipe(models.Model):
    title = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='img')
    category = models.CharField(max_length=60)
    ingredients = models.TextField(null=True)
    description = models.TextField(null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f'{self.title}'
