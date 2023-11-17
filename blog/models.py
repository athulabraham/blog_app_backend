from django.db import models

# Create your models here.
class BlogModel(models.Model):
    title=models.CharField(default="",max_length=100)
    user_id=models.CharField(default="",max_length=100)
    post=models.CharField(default="",max_length=4000)
    
    
class UserModel(models.Model):
    name=models.CharField(default="",max_length=100)
    image=models.CharField(default="",max_length=4000)
    email=models.CharField(default="",max_length=100)
    password=models.CharField(default="",max_length=100)