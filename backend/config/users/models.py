from django.contrib.auth.models import AbstractUser
from django.db import models

class RestaurantUser(AbstractUser):
    email = models.EmailField(unique=True)
    restaurant_name = models.CharField(max_length=255)
    address = models.TextField()
    phone = models.CharField(max_length=15)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'restaurant_name', 'address', 'phone']

    def __str__(self):
        return self.restaurant_name
       
