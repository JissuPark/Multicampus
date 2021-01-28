from rest_framework import serializers
from .models import Student


class Stdserializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
