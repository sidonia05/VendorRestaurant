from django.urls import path
from userextends import views

urlpatterns = [
    path('create-user/', views.UserCreateView.as_view(), name='create_user'),
    path('login/', views.UserLoginView.as_view(), name='user_login'),
]
