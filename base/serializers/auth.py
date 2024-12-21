# auth_app/serializers.py
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from base.models.auth import Role
from django.contrib.auth.models import User



class UserSerializer(serializers.ModelSerializer):
    role = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'role']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        role_name = validated_data.pop('role')  # Extract role from validated data
        user = User.objects.create_user(**validated_data)
        
        # Create the role associated with the user
        role = Role.objects.create(user=user, name=role_name, description=f"{role_name} role")
        
        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(username=data['username'], password=data['password'])
        if user is None:
            raise serializers.ValidationError('Invalid credentials')
        return user


class TokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = RefreshToken
        fields = ['access', 'refresh']
