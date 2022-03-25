from django.contrib.auth import authenticate
# from django.contrib.auth.models import User
from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'address', 'is_student', 'is_teacher', 'is_ai')


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
        'id', 'username', 'first_name', 'last_name', 'address', 'is_student', 'is_teacher', 'is_ai', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['username'],
            password=validated_data['password'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            address=validated_data['address'],
            is_student=validated_data['is_student'],
            is_teacher=validated_data['is_teacher'],
            is_ai=validated_data['is_ai'])
        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError('Invalid Credentials.')
