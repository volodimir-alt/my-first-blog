from django.urls import path
from blog.views import  post_list
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
]