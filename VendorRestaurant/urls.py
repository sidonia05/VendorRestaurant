
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views
from django.urls import path, include

from userextend.forms import AuthenticationNewForm, PasswordChangeNewForm




urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('', include('employee.urls')),
    path('', include('task.urls')),
    path('', include('restaurantmenu.urls')),
    path('', include('recipes.urls')),
    path('', include('cart.urls')),
    path("login/", views.LoginView.as_view(form_class=AuthenticationNewForm), name="login"),
    path("password_change/", views.PasswordChangeView.as_view(form_class=PasswordChangeNewForm), name="password_change"),

    path('', include('django.contrib.auth.urls')),


    path('', include('userextend.urls')),
    path('', include('orders.urls')),
    path('', include('contact.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
