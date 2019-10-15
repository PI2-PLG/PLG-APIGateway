from users.models import CustomUser
from django.contrib.auth.models import User
from rest_framework import serializers

class CustomUserSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=200)
    email = serializers.EmailField()
    username = serializers.CharField(max_length=200)
    notification_token = serializers.CharField(max_length=255)

    class Meta:
        model = CustomUser
        fields = ['name','email','username','notification_token']