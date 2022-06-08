from django.db import models
from authemail.models import EmailUserManager
from authemail.models import EmailAbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator
# Create your models here.
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, AbstractUser
from rest_framework_simplejwt.tokens import RefreshToken
import math
import random



class MyUser(EmailAbstractUser):
			cool_name = models.CharField(
			verbose_name='Username',

			max_length=150,
			validators=[UnicodeUsernameValidator]

			)
			REQUIRED_FIELDS = ['password', 'cool_name']
			gender_choices=[('Female', 'Female'), ('Male', 'Male')]
			Gender=models.CharField(max_length=255, choices=gender_choices)
			is_completely_verified = models.BooleanField(default=False)
			USERNAME_FIELD = 'email'

			objects = EmailUserManager()


