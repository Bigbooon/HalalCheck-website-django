from django.urls import path
from .views import *

urlpatterns = [
    path('', posts_list, name='posts_list_url'),
    path('post/<str:slug>/', post_detail, name='post_detail_url'),
    path('tag/<str:slug>', tag_detail, name='tag_detail_url'),
    path('aboutUs', aboutUs, name='aboutUs_url'),
    path('home', home, name='home_url'),
]