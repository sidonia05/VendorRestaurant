from django.urls import path

from restaurantmenu.views import ProductView

urlpatterns = [
    path('menu/', ProductView.as_view(), name='menu-homepage'),
]

