import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(max_length=30, unique=True, default=' ')
    # image1 = models.ImageField(upload_to='pics')
    # image2 = models.ImageField(upload_to='pics')
    desc = models.TextField()
    email = models.EmailField(max_length=100)
    degree = models.TextField(max_length=100)
    job_role = models.CharField(max_length=100)

USERNAME_FIELD ='username'
REQUIRED_FIELDS =[]    