from django.db import models

# Create your models here.


class FormLink(models.Model):
    link = models.CharField(max_length=500)
    title = models.CharField(max_length=300)
    description = models.TextField()
