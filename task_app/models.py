from django.db import models

# Create your models here.

class Task(models.Model):
    name =  models.CharField(max_length=200)
    description = models.TextField()
    completed = models.BooleanField(default=False)

    