from django.db import models

class User(models.Model):
    email = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    name = models.CharField(max_length=255)

    

class ProcessGuideline(models.Model):
    step_name = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    step_detail = models.TextField()
    step_number = models.BigIntegerField()


class Stock(models.Model):
    material_name = models.CharField(max_length=255)
    quantity = models.IntegerField()
    place = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

  

class Order(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    address = models.TextField()
    product_name = models.CharField(max_length=255)
    quantity = models.IntegerField()
    deadline = models.BigIntegerField()
    weight = models.FloatField()
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled')
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

   

class Chat(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    sender = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.BigIntegerField()


