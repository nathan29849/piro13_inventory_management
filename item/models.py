from django.db import models

class Account(models.Model):
    name = models.CharField(max_length=100)
    call = models.CharField(max_length=100)
    address = models.TextField()

class Item(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(blank=True)
    content = models.TextField()
    price = models.CharField(max_length=100)
    amount = models.CharField(max_length=100)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)