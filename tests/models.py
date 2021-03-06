from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Band(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Album(models.Model):
    band = models.ForeignKey(Band, models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
