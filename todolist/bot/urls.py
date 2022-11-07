from django.urls import path

from bot import views

urlapetterns = [
    path('verify', views.VerificationView.as_view(), name='verify-user')
]