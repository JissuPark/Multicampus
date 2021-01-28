from django.db import models


class Main(models.Model):
    # workspace 제목
    name = models.CharField(max_length=30)
    # workspace 설명
    about = models.CharField(max_length=200)
