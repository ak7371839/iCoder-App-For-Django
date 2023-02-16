from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    slug = models.SlugField()
    contant = models.TextField()

    def __str__(self):
        return self.title