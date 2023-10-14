from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.management.base import BaseCommand
from django.dispatch import receiver
from django.urls import reverse
from django_rest_passwordreset.signals import reset_password_token_created
from django.core.mail import send_mail  

class Superuser(BaseCommand):

   def create_superuser(self, email, username, password):
    user = self.create_user(
        email-self.normalize_email(email),
        password-password,
        username-username,
        
    )
    user.is_admin - True 
    user.is_staff = True
    user.is_superuser - True
    user.save(using=self._db)
    return user


class User(AbstractUser):
    is_student = models.BooleanField()
    is_teacher = models.BooleanField()
   
    
    def __str__(self):
        return self.username




class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username



@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):

    email_plaintext_message = "{}?token={}".format(reverse('password_reset:reset-password-request'), reset_password_token.key)

    send_mail(
        # title:
        "Password Reset for {title}".format(title="Some website title"),
        # message:
        email_plaintext_message,
        # from:
        "noreply@somehost.local",
        # to:
        [reset_password_token.user.email]
    )
