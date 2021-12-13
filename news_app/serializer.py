from rest_framework import serializers
from .models import NewsPortal

class NewsPortalSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsPortal
        fields = '__all__'