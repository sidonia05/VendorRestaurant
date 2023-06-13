from django.urls import path

from restaurantmenu import views
from restaurantmenu.views import AllProductsView, BakeryListView, MexicanListView, FastFoodListView, PizzaListView, \
    SaladListView, TraditionalFoodListView

urlpatterns = [
    path('menu/', AllProductsView.as_view(), name='menu-homepage'),
    path('menu/bakery', BakeryListView.as_view(), name='menu-bakery'),
    path('menu/mexican-food', MexicanListView.as_view(), name='menu-mexican'),
    path('menu/fast-food', FastFoodListView.as_view(), name='menu-fastfood'),
    path('menu/pizza', PizzaListView.as_view(), name='menu-pizza'),
    path('menu/salad', SaladListView.as_view(), name='menu-salad'),
    path('menu/traditional', TraditionalFoodListView.as_view(), name='menu-traditional'),
    path('search/', views.search, name='search'),
]

