from django.db import models
from django.contrib.auth.models import User 

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField(null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user') 
    date_created = models.DateTimeField(auto_now_add=True)
    date_edited = models.DateTimeField(auto_now=True)
    public = models.BooleanField()

    def __str__(self):
        return self.title



# Create your models here.
