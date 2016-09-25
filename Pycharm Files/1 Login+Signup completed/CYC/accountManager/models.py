from __future__ import unicode_literals

from django.db import models

# Create your models here.


class UserInformation(models.Model):
    userName=models.CharField(max_length=50)
    emailID=models.CharField(max_length=200)
    password=models.CharField(max_length=200)
    mobileNum=models.IntegerField(default=0000000000)
    currentToken=models.CharField(max_length=50)