from .models import Post
from rest_framework import serializers
from django.core.validators import FileExtensionValidator
from authentication.models import MyUser as User


class PostSerializer(serializers.ModelSerializer):
	file_uploaded=serializers.FileField(validators=[FileExtensionValidator(allowed_extensions=['jpg','jpeg','png'])])

	class Meta:
		model=Post
		exclude = ('Design_photo', )

	def create(self, validated_data):
		validated_data['Design_photo']=validated_data['file_uploaded']
		del validated_data['file_uploaded']	 
		user_data=Post.objects.create(**validated_data)
		return user_data

