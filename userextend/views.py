from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.generic import CreateView

from cart.models import CartItem, Cart
from userextend.forms import UserForm, AuthenticationNewForm


class UserCreateView(CreateView):
    template_name = 'userextend/create_user.html'
    form_class = UserForm
    success_url = '/login/'

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationNewForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = AuthenticationNewForm()
    return render(request, 'registration/login.html', {'form': form})



@login_required
def profile(request):
    user = request.user
    cart_items = CartItem.objects.filter(user=user)
    return render(request, 'registration/profile.html', {'user': user, 'cart_items': cart_items})
