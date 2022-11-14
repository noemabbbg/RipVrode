from django.db import models

# Create your models here.
from django.db import models

class range(models.Model):
    rangeName = models.CharField(unique=True, max_length=30, default=None)


class genre(models.Model):
    name = models.CharField(max_length=45, default=None)
    quantity = models.IntegerField(blank=True, null=True, default=None)
    image = models.ImageField(default=None)

class title(models.Model):
    genre_id = models.ForeignKey(genre, models.DO_NOTHING, default=None)
    name = models.CharField(max_length=45, default=None)
    pg = models.IntegerField(blank=True, null=True, default=None)
    release = models.IntegerField(blank=True, null=True, default=None)
    price = models.IntegerField(blank=True, null=True, default=None)
