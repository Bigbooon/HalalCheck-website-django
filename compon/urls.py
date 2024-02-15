from django.urls import path
from .views import *

urlpatterns = [
    path('', comp_list, name='comp_list_url'),
    path('tag/<str:slug>', comp_tag_detail, name='comp_tag_detail_url'),
]
