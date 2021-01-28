from django.db import models


class Student(models.Model):
    number = models.IntegerField()
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    major = models.CharField(max_length=30)
