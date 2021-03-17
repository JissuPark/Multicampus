from django.db import models

class GuGudan(models.Model):
    id = models.AutoField(primary_key=True)
    dan = models.IntegerField()
