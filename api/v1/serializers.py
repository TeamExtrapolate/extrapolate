from rest_framework import serializers
from user.models import User
from django.contrib.auth import password_validation


class SignupSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField()
    password2 = serializers.CharField()

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        extra_kwargs = {'password1': {'write_only': True}, 'password2': {'write_only': True}}

    def validate(self, data):
        password1 = data.get('password1',None)
        password2 = data.get('password2',None)
        if password1 and password2 and password1 != password2:
            raise serializers.ValidationError('Passwords donot match')
        return data
