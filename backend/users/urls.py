from django.urls import path

from .views import *


app_name = "users"

urlpatterns = [
    path('api/users', UsersView.as_view(), name='users'),
]
