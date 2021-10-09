from django.db import models


class Customer(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField('Name', max_length=30, default="")
    email = models.EmailField('Email', max_length=150)
    address = models.CharField('Address', max_length=150, default="")
