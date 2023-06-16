from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView

from restaurantmenu.models import Product
from django.shortcuts import render
from django.db.models import Q


# Create your views here.
class AllProductsView(View):
    def get(self, request):
        products = Product.objects.all()
        return render(request, 'menu/menu-homepage.html', {'products': products})


class BakeryListView(ListView):
    model = Product
    template_name = 'menu/menu-homepage.html'
    context_object_name = 'products'
    ordering = ['name']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        products = Product.objects.filter(type_prod=1).all()
        context['products'] = products
        return context


class MexicanListView(ListView):
    model = Product
    template_name = 'menu/menu-homepage.html'
    context_object_name = 'products'
    ordering = ['name']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        products = Product.objects.filter(type_prod=2).all()
        context['products'] = products
        return context


class FastFoodListView(ListView):
    model = Product
    template_name = 'menu/menu-homepage.html'
    context_object_name = 'products'
    ordering = ['name']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        products = Product.objects.filter(type_prod=3).all()
        context['products'] = products
        return context


class PizzaListView(ListView):
    model = Product
    template_name = 'menu/menu-homepage.html'
    context_object_name = 'products'
    ordering = ['name']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        products = Product.objects.filter(type_prod=4).all()
        context['products'] = products
        return context


class SaladListView(ListView):
    model = Product
    template_name = 'menu/menu-homepage.html'
    context_object_name = 'products'
    ordering = ['name']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        products = Product.objects.filter(type_prod=5).all()
        context['products'] = products
        return context

class TraditionalFoodListView(ListView):
    model = Product
    template_name = 'menu/menu-homepage.html'
    context_object_name = 'products'
    ordering = ['name']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        products = Product.objects.filter(type_prod=6).all()
        context['products'] = products
        return context



def search(request):
    search_value = request.GET.get('value')
    products = Product.objects.filter(name__icontains=search_value)
    return render(request, 'menu/search_results.html', {'products': products, 'search_value': search_value})
