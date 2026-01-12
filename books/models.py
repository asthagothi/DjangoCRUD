from django.db import models
from django.contrib.auth.models import user

class Book(models.Model):
    user = models.ForeignKey(user, on_delete=models.CASCADE) # type: ignore
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    description = models.TextField()
    published_date = models.DateField()

    def __str__(self):
        return self.title
# Create your models here.
