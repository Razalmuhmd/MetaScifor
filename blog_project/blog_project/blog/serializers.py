# serializers.py
from rest_framework import serializers
from .models import Footballer

class FootballerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Footballer
        fields = ['id', 'title', 'content', 'image', 'created_at', 'updated_at']
