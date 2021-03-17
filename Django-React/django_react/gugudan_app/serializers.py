from rest_framework import serializers
from .models import GuGudan


class GuGudanSerializer(serializers.ModelSerializer):
    class Meta:
        model = GuGudan
        fields = ['id', 'dan']
