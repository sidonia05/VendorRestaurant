from django.shortcuts import render, get_object_or_404
from django.views import View

from recipes.models import Recipe

class RecipeView(View):
    def get(self, request):
        recipes = Recipe.objects.all()
        return render(request, 'recipe/recipe.html', {'recipes': recipes})

class RecipeDetailsView(View):
    def get(self, request, pk):
        recipe = get_object_or_404(Recipe, pk=pk)
        recipes = [recipe]  # Wrap the recipe in a list
        return render(request, 'recipe/recipe_details.html', {'recipes': recipes})




