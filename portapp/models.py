from django.db import models

# Create your models here.


class Portfolio(models.Model):
    objects = None

    username = models.CharField(max_length=30)
    image1 = models.ImageField(upload_to='pics')
    image2 = models.ImageField(upload_to='pics')
    mail = models.CharField(max_length=100)
    desc = models.TextField()
    degree = models.TextField(max_length=100)
    job_role = models.CharField(max_length=100)
