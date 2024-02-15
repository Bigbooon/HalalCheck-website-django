from django.urls import path
from .views import *

urlpatterns = [

    path('', SignupPage, name='signup_url'),
    path('login/', LoginPage, name='login_url'),
    path('home/', HomePage, name='home_url'),
    path('logout/', LogoutPage, name='logout_url'),
    path('home/', main, name='main_url'),
]
