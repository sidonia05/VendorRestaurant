from django.urls import path

from recipes.views import RecipeView, RecipeDetailsView

urlpatterns = [
    path('menu/recipe/', RecipeView.as_view(), name = 'recipe'),
    path('menu/recipe/<int:pk>/', RecipeDetailsView.as_view(), name='recipe-details'),
]