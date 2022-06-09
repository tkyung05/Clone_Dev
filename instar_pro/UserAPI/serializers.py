from rest_framework import serializers
from .models import User

class UserRegistrationSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ('email', 'password', 'nickname', 'profile_image')
        extra_kwargs = {"password": {"write_only":True}}
    
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user