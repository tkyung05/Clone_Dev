from rest_framework import serializers
from .models import User
from rest_framework_jwt.settings import api_settings
from django.contrib.auth import authenticate
from django.contrib.auth.models import update_last_login


class UserRegistrationSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ('email', 'password', 'nickname', 'profile_image')
        extra_kwargs = {"password": {"write_only":True}}
    
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


JWT_PAYLOAD_HANDLER = api_settings.JWT_PAYLOAD_HANDLER
JWT_ENCODE_HANDLER = api_settings.JWT_ENCODE_HANDLER

class UserLoginSerializer(serializers.Serializer):

    email = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=128, write_only=True)
    token = serializers.CharField(max_length=255, read_only=True)

    def validate(self, data):
        email = data.get("email", None)
        password = data.get("password", None)
        user = authenticate(email=email, password=password)
        if user is None:
            raise serializers.ValidationError(
        "A user with this email and password is not found."
        )
        try:
            payload = JWT_PAYLOAD_HANDLER(user)
            payload['nickname'] = User.objects.get(email=user).nickname
            payload['profile_image'] = str(User.objects.get(email=user).profile_image)
            jwt_token = JWT_ENCODE_HANDLER(payload)
            update_last_login(None, user)

        except User.DoesNotExist:
            raise serializers.ValidationError(
        "User with given email and password does not exists"
        )
        
        return {
            'email': user.email,
            'token': jwt_token
        }