from rest_framework import serializers
from .models import NewsPortal
from django.contrib.auth import get_user_model

class NewsPortalSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsPortal
        fields = ['title','image_link','sub_title','main_content']

class UserDetailsSerializer(serializers.ModelSerializer):
    
    class Meta:
        user  = get_user_model()
        model = user
        fields = ['email','first_name','last_name','mobile','last_login']
        extra_kwargs = {'password': {'write_only': True}}
