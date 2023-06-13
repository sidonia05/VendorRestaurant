from django.urls import path
from userextend import views

urlpatterns = [
    path('create-user/', views.UserCreateView.as_view(), name='create_user'),
    path('login/', views.login_view, name='login'),
]
