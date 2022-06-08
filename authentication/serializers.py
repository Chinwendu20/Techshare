from rest_framework import serializers
from .models import  MyUser

class UserSerializer(serializers.Serializer):
		username=serializers.CharField()
		email=serializers.EmailField()
		password=serializers.CharField()

			




class CompleteProfileSerializer(serializers.Serializer):

		First_name=serializers.CharField()
		Last_name=serializers.CharField()
		gender_choices=[('Female', 'Female'), ('Male', 'Male')]
		Gender=serializers.ChoiceField(choices=gender_choices, allow_blank=False)

		

