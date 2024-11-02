from django.contrib import admin
from django.urls import path
from userauth.views import UserAuthView

urlpatterns = [
    path('login', UserAuthView.as_view(),name='login'),
]
