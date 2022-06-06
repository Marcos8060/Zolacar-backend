from rest_framework import serializers
from .models import *



class RegisterUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=50,min_length=6,write_only=True)
    class Meta:
        model = NewUser
        fields = ['email','user_name','password']
    
    def create(self,validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'


class FeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Featured
        fields = '__all__'