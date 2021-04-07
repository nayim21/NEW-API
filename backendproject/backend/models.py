from django.db import models
from django.contrib.auth.models import User
#from datetime import datetime
# Create your models here.
class article(models.Model):
    #id=models.IntegerField(primary_key=True)
    title=models.CharField(max_length=20)
    body=models.TextField()
    image=models.ImageField(default='', upload_to='pictures/', null=True)
    date=models.DateTimeField()
    author=models.CharField(max_length=20)
    fav=models.BooleanField(default=True)

# Create your models here.
