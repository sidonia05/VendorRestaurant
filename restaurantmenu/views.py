from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.views import View

from restaurantmenu.models import Product


# Create your views here.
class ProductView(View):
    def get(self,request):
        products = Product.objects.all()
        return render(request,'menu/menu-homepage.html',{'products':products})
