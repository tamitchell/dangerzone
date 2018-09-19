# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import AbstractUser


from django.db import models

# Create your models here.
class Animals(models.Model):
    name = models.CharField(max_length=100, default="")
    species = models.CharField(max_length=100, default="")
    picture = models.TextField()
    region =  models.TextField()
    habitat = models.CharField(max_length=100, default="")
    endangeredLvl = models.CharField(max_length=100, default="")
    population = models.TextField()
    about = models.TextField()

    def __str__(self):
        return self.name

class News(models.Model):
    title = models.CharField(max_length=100, default="")
    imageURL = models.TextField()
    author = models.CharField(max_length=100, default="")
    description = models.TextField()
    article = models.TextField()

    def __str__(self):
        return self.title

class UserProfile(AbstractUser):
    animal_list = ArrayField(models.TextField(), null=True, blank=True)

    def __str__(self):
        return self.email