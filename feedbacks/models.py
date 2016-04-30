# -*- coding: utf-8 -*-
from django.db import models

class Feedback(models.Model):
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=50)
    message = models.TextField(max_length=100)
    from_email = models.EmailField()
    create_date = models.DateField(auto_now_add=True)