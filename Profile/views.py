from django.shortcuts import render
from rest_framework.views import APIView 
from django.contrib.auth import get_user_model
from authentication.models import MyUser as User
from .serializers import PostSerializer
from django.conf import settings
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
import urllib.request
from .models import Post
from drf_yasg.utils import swagger_auto_schema
from rest_framework.parsers import FileUploadParser, MultiPartParser, FormParser




class PostView(APIView):
	serializer_class=PostSerializer
	parser_classes = (MultiPartParser,)
	permission_classes = (IsAuthenticated,)
	@swagger_auto_schema(request_body=PostSerializer)
	def post(self, request, format=None):
		serializer=self.serializer_class(data=request.data)
		if serializer.is_valid():
			serializer.validated_data['Design_photo']=serializer.validated_data['file_uploaded']
			serializer.validated_data['user']=request.user
			del serializer.validated_data['file_uploaded']
			user_data=Post.objects.create(**serializer.validated_data)
			content={	'user':user_data.user.email, 'Design_photo':user_data.Design_photo.url,
			'Link':user_data.Link, 'Design_title':user_data.Design_title, 'Design_brief': user_data.Design_brief}
			return Response(content, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PostUpdateDestroyView(APIView):
	serializer_class=PostSerializer
	parser_classes = (MultiPartParser,)
	permission_classes = (IsAuthenticated,)
	@swagger_auto_schema(request_body=PostSerializer)
	def patch(self, request, id, format=None):
		try:
			user=request.user
			post = Post.objects.filter(user=user).get(id=id)
		except Post.DoesNotExist:
			return Response({'message':'Data does not exist'},status=status.HTTP_400_BAD_REQUEST)
		serializer = self.serializer_class(post, data=request.data, partial=True)
		if serializer.is_valid():
			user_data=serializer.save()
			content={	'user':user_data.user.email, 'Design_photo':user_data.Design_photo.url,
			'Link':user_data.Link, 'Design_title':user_data.Design_title, 'Design_brief': user_data.Design_brief}
			return Response(content, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request,id, format=None):
		try:
			user=request.user
			post = Post.objects.filter(user=user).get(id=id)				
		except Post.DoesNotExist:
			return Response({'message':'Data does not exist'},status=status.HTTP_400_BAD_REQUEST)
		post.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)

class PostGetUserView(APIView):
	serializer_class=PostSerializer
	parser_classes = (MultiPartParser,)
	permission_classes = (IsAuthenticated,)
	def get (self, request, id, format=None):
		try:
			user_data = Post.objects.get(id=id)
			serializer = self.serializer_class(user_data)
		except Post.DoesNotExist:
			return Response(status=status.HTTP_204_NO_CONTENT)
		return Response(serializer, status=status.HTTP_200_OK)
