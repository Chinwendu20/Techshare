from django.db import models
from django.db import models
from django.conf import settings
from authentication.models import MyUser as User
from cloudinary.models import CloudinaryField
import uuid
from django.contrib.sessions.models import Session




class Post(models.Model):
	user=models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
	Design_photo=CloudinaryField('Design_photo')
	Link = models.CharField( max_length=200)
	Design_title=models.CharField( max_length=200)
	Design_brief=models.CharField( max_length=200)
