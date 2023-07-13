import datetime

import django
from django.contrib.auth.models import User
from django.db import models


# class Payment(models.Models):
#     user = models.ForeignKey(Account, on_delete=models.CASCADE)
#     payment_id = models.CharField(max_length=100)
#     payment_method = models.CharField(max_length=100)
#     amount_paid = models.CharField(max_length=100)
#     status = models.CharField(max_length=100)
#     created_at = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return self.payment_id
#
class Order(models.Model):
    number = models.IntegerField(null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
