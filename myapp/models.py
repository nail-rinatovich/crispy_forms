from django.db import models
from django import forms
class Contact(models.Model):
    Имя = models.CharField(max_length=100)
    Телефон = models.CharField(max_length=20)
    Email = models.EmailField()

    def __str__(self):
        return self.Имя
