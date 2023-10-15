
from django.urls import path, include
from . import views

urlpatterns = [
    path('create_token/', views.create_token, name='create_token'),
    # path('signup/', views.signup, name='signup'),
    # path('login/', views.login, name='login'),
    # path('forget_password/', views.forget_password, name='forget_password'),

    # path('change_password/', views.change_password, name='change_password'),
    # path('change_password_code_check/', views.change_password_code_check, name='change_password_code_check'),

    # path('valid_change_password_token/', views.valid_change_password_token, name='valid_change_password_token'),
    
    # path('save_on_boarding/', views.save_on_boarding, name='save_on_boarding'),
    # path('load_basic_data/', views.load_basic_data, name='load_basic_data'),

    # path('change_language/', views.change_language, name='change_language'),
    # path('logout/', views._logout, name='logout'),
]

