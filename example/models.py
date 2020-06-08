from django.db import models
from datetime import datetime
# Create your models here.
class Simple(models.Model):
     text = models.CharField(max_length=10)
     number = models.IntegerField(null=True)
     url = models.URLField(null=True)
     created_at = models.DateTimeField(default= datetime.now, blank=True)
     updated_at = models.DateTimeField(default= datetime.now, blank=True)

     def __str__(self):
         return self.text

class Language(models.Model):
    name = models.CharField(max_length=20)


class Framework(models.Model):
    name = models.CharField(max_length=20)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
