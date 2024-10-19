from django.db import models

# Create your models here.
class User(models.Model):
    name=models.CharField(max_length=30)
    city=models.CharField(max_length=30)
    email=models.CharField(max_length=30)
    password=models.CharField(max_length=30)

    class Meta:
        db_table='entry'

class Blogs(models.Model):
    title = models.CharField(max_length=50, blank=True, null=True)
    description = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'blogs'