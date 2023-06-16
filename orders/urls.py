from django.urls import path

from orders import views

urlpatterns =[
    path('cart/checkout/place_order/', views.place_order, name = 'place_order')
]