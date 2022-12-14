
#from turtle import title
from django.db import models
from django.contrib.auth.models import AbstractUser
import datetime
# from . import helpers



class User(AbstractUser):
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    username = models.CharField(max_length=200, unique=True)
    email = models.CharField(max_length=200, default='n/a')
    password = models.CharField(max_length=200)
    # title = None
    balance = models.FloatField(default=0.0)
    accountnumber= models.IntegerField( unique = True)
    # balance = 0
    # account_number = helpers.generate_account_number()
    # last_login = models.CharField(default=datetime.datetime.now(),max_length=200)
    # completed = models.BooleanField(default=False)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.title


class Deposit(models.Model):
    amount= models.FloatField()
    
