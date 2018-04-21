from __future__ import unicode_literals
from django.db import models


class profile(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField(default='description default text')

    def __unicode__(self):
        return self.name


class product(models.Model):
    name = models.CharField(max_length=32)
    description = models.TextField(default='description default text')
    image = models.ImageField(upload_to='product_image', blank=True, null=True)

    def __str__(self):
        return self.name

