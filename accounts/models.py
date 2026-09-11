from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    ROLE_ADMIN = 'admin'
    ROLE_FREELANCER = 'freelancer'
    ROLE_CLIENT = 'client'

    ROLE_CHOICES = [
        (ROLE_ADMIN, 'Admin'),
        (ROLE_FREELANCER, 'Freelancer'),
        (ROLE_CLIENT, 'Client'),
    ]

    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default=ROLE_CLIENT)
    phone = models.CharField(max_length=20, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    location = models.CharField(max_length=100, blank=True)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    def is_admin(self):
        return self.role == self.ROLE_ADMIN

    def is_freelancer(self):
        return self.role == self.ROLE_FREELANCER

    def is_client(self):
        return self.role == self.ROLE_CLIENT

    def get_profile_picture_url(self):
        if self.profile_picture:
            return self.profile_picture.url
        return '/static/images/default_avatar.png'

    def __str__(self):
        return f"{self.username} ({self.role})"
