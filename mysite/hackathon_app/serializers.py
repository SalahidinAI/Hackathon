from rest_framework import serializers
from .models import *
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('username', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = UserProfile.objects.create_user(**validated_data)
        return user

    def to_representation(self, instance):
        refresh = RefreshToken.for_user(instance)
        return {
            'user': {
                'username': instance.username,
                'email': instance.email,
            },
            'access': str(refresh.access_token),
            'refresh': str(refresh),
        }


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Неверные учетные данные")

    def to_representation(self, instance):
        refresh = RefreshToken.for_user(instance)
        return {
            'user': {
                'username': instance.username,
                'email': instance.email,
            },
            'access': str(refresh.access_token),
            'refresh': str(refresh),
        }


class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField()


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'


# class Serializer(serializers.ModelSerializer):
#     class Meta:
#         model =
#         fields = '__all__'
#
#
# class Serializer(serializers.ModelSerializer):
#     class Meta:
#         model =
#         fields = '__all__'
#
#
# class Serializer(serializers.ModelSerializer):
#     class Meta:
#         model =
#         fields = '__all__'
#
#
# class Serializer(serializers.ModelSerializer):
#     class Meta:
#         model =
#         fields = '__all__'
#
#
# class Serializer(serializers.ModelSerializer):
#     class Meta:
#         model =
#         fields = '__all__'
#
#
# class Serializer(serializers.ModelSerializer):
#     class Meta:
#         model =
#         fields = '__all__'
#
#
# class Serializer(serializers.ModelSerializer):
#     class Meta:
#         model =
#         fields = '__all__'
#
#
# class Serializer(serializers.ModelSerializer):
#     class Meta:
#         model =
#         fields = '__all__'
#
#
# class Serializer(serializers.ModelSerializer):
#     class Meta:
#         model =
#         fields = '__all__'
