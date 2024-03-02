
from django.urls import path, include
from . import views

urlpatterns = [
    path(
        'create_token/', 
        views.create_token, 
        name='create_token'
    ),
    path(
        'redirect/:token/', 
        views.redirect, 
        name='redirect'
    ),
]

