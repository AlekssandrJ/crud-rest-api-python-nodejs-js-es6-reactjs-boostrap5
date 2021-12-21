from django.db import models

# Create your models here.

class Task(models.Model):
    TaskId = models.AutoField(primary_key=True)
    TaskName = models.CharField(max_length=500)