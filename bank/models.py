from django.db import models

# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=25)
    number = models.IntegerField()
    email = models.EmailField(max_length=50)
    current_balance = models.IntegerField()

    def __str__(self):
        return self.name

class Transfer(models.Model):
    sender_name = models.CharField(max_length=25)
    amount = models.IntegerField()
    receiver_name = models.CharField(max_length=25)

    def __str__(self):
        return self.sender_name
