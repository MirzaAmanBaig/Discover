from django.db import models

# Create your models here.

class Destination(models.Model):
    name=models.CharField(max_length=20)
    image=models.ImageField(upload_to='pics')
    price=models.IntegerField()
    desc=models.TextField()
    link=models.URLField()

class Contact(models.Model):
    firstname=models.CharField(max_length=20)
    lastname=models.CharField(max_length=20)
    email=models.CharField(max_length=50)
    feedback=models.TextField()