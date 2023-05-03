from django.db import models

class Any(models.Model):
    name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)