from django.db import models
from django.contrib.auth.models import User


# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     city = models.CharField(max_length=30)

#     def __str__(self):
#         return self.user.username.upper()