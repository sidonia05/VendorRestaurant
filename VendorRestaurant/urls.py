
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('', include('employee.urls')),
    path('', include('task.urls')),
    path('', include('restaurantmenu.urls')),
    path('', include('recipes.urls')),
    path('', include('userextends.urls')),



] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
