from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from .models import RestaurantUser

class RestaurantUserSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)
    
    class Meta:
        model = RestaurantUser
        fields = ['email', 'username', 'restaurant_name', 'address', 'phone', 'password1', 'password2']
     
    def validate(self, data):
        if data['password1'] !=  data['password2']:
            raise serializers.ValidationError({"password": "Passwords do not match!"})
        return data
    
    def create(self, validated_data):
        validated_data.pop('password2')  # Remove confirm password before saving
        
        user = RestaurantUser.objects.create(
            email=validated_data['email'],
            username=validated_data['username'],
            restaurant_name=validated_data['restaurant_name'],
            address=validated_data['address'],
            phone=validated_data['phone']
        )
        user.set_password(validated_data['password1'])  # Hash password
        user.save()
        return user
    



