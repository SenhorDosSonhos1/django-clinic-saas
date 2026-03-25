from django.db import models

#Custom User model imports
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):

    ROLE_CHOICES = (
        ('staff', 'Staff'),
        ('doctor', 'Doctor'),
        ('admin', 'Admin'),
    )
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='admin')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email