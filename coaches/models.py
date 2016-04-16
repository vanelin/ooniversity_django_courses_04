# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User


class Coach(models.Model):
    user = models.OneToOneField(User)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=1, choices=(
        ('M', 'Male'),
        ('F', 'Female')
    ))
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=255)
    skype = models.CharField(max_length=50)
    description = models.TextField()

    def __unicode__(self):              # __str__ on Python 3
        return self.user.username

    def name(self):
        return self.user.first_name
    name.short_description = 'name'

    def last_name(self):
        return self.user.last_name
    last_name.short_description = 'last_name'
