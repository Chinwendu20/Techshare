from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views


urlpatterns = [
    path('create/', views.PostView.as_view()),
    path('modify/<int:id>/', views.PostUpdateDestroyView.as_view()),
    path('view/<int:id>/', views.PostGetUserView.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)
