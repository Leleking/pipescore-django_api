from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Project(models.Model):
    term = models.CharField(max_length=100)
    description = models.TextField()
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
