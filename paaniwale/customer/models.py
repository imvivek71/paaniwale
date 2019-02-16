from django.db import models

# Create your models here.
class Post(models.Model):
    FirstName = models.CharField(max_length=15)
    MiddleName = models.CharField(max_length=15)
    LastName = models.CharField(max_length=15)
    Age = models.CharField(max_length=15)
    Gender = models.CharField(max_length=15)
