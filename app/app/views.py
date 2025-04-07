from django.shortcuts import render
import requests
from core.models import Recipe, Tag, Ingredient

# def home(request):
#     recipes = Recipe.objects.all()
#     tags = Tag.objects.all()
#     ingredients = Ingredient.objects.all()
#     print(f"Anzahl Posts: {recipes.count()}")
#     for recipe in recipes:
#         print(recipe.title)
#     return render(request, 'home.html', {'recipes': recipes, 'tags': tags, 'ingredients': ingredients})


def home(request):
    token = request.user.auth_token.key if hasattr(request.user, 'auth_token') else None
    api_url = "http://127.0.0.1:8000/api/recipe/recipes"

    headers = {'Authorization': f"Token {token}"}
    response = requests.get(api_url, headers=headers)
    
    data = response.json() if response.status_code == 200 else {}
    print(data)
    return render(request, "home.html", {"data": data})
