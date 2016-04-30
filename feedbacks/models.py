# -*- coding: utf-8 -*-
from django.db import models

class Feedback(models.Model):
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=50)
    message = models.TextField(max_length=100)
    from_email = models.EmailField()
    create_date = models.DateField(verbose_name="Created on date", auto_now_add="True")

    def __unicode__(self):              # __str__ on Python 3
        return (self.name)