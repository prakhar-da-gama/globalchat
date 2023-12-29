# chat/urls.py
from django.urls import path
from .views import login_view, register_view, post_message

urlpatterns = [
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('post-message/', post_message, name='post_message'),
]
