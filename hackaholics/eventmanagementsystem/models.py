from django.db import models

# Create your models here.
class credentials(models.Model):
    name=models.TextField()
    email=models.TextField()
    password=models.TextField()


class events(models.Model):
    organizeremail=models.TextField()
    name=models.TextField()
    description=models.TextField()
    datetime=models.TextField()
    location=models.TextField()
    eventtype=models.TextField()
    category=models.TextField()
    utubelink=models.TextField()
    
    
    
