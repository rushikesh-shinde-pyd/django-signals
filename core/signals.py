from . import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.signals import user_logged_in, user_logged_out


@receiver(user_logged_in, sender=User)
def log_user_logged_in(sender, request, user, **kwargs):
    print(user.username.lower(), 'logged in successfully from Signals')


@receiver(user_logged_out, sender=User)
def log_user_logged_out(sender, request, user, **kwargs):
    print(user.username.lower(), 'logged out successfully from Signals')
    