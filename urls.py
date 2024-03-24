
from django.urls import path, include
from . import views

urlpatterns = [
    path(
        'create_token/', 
        views.create_token, 
        name='token_manager__create_token'
    ),
    path(
        'redirect/:token/', 
        views.redirect, 
        name='token_manager__redirect'
    ),
    path(
        'check_is_valid/', 
        views.check_is_valid, 
        name='token_manager__check_is_valid'
    ),
]

