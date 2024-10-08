from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

class UserRegistrationModels(AbstractUser):
    agree_to_term = models.BooleanField(default=False)

    def __str__(self):
        return self.username

    # optional
    groups = models.ManyToManyField(Group, related_name='UserRegistrationModels')
    user_permissions = models.ManyToManyField(Permission, related_name='UserRegistrationModels_Permission')