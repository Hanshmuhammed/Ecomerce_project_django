from django.db import models

# Create your models here.
class site_setting(models.Model):
    banner=models.ImageField(upload_to='media/site/')
    caption=models.TextField()