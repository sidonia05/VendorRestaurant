from django.urls import path

from orders import views

urlpatterns =[
    path('cart/order/place_order/', views.place_order, name = 'place_order')
]