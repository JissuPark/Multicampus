from django.db import models


class Todojs(models.Model):
    title = models.CharField(max_length=255)

