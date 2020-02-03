from django.db import models
from datetime import datetime


class Realtor(models.Model):
    name = models.CharField(max_length=50)
    hire_date = models.DateField(default=datetime.now, blank=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    description = models.TextField()
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    is_mvp = models.BooleanField(default=True)

    def __str__(self):
        return self.name
