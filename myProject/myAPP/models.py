from django.db import models
from django.utils import timezone
# Create your models here.


class Book (models.Model):
    name = models.CharField(max_length=20)
    pageNumber = models.IntegerField()
    genre= models.CharField(max_length=20)
    publishDate= models.DateField(default=timezone.now)
   
    def __str__(self):
        return self.name