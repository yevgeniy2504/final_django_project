from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.http import HttpResponseBadRequest
from .forms.category_add_form import CategoryForm
from .forms.new_user_profile_form import AuthorForm
from .forms.new_recipe_form import RecipeForm
from .forms.add_ingridient import IngredientForm
from .models import Recipe, Author


def generate_links():
    return [
        {'url': reverse('index'), 'text': 'Главная'},
        {'url': reverse('create_recipe'), 'text': 'Создать рецепт'},
        {'url': reverse('create_category'), 'text': 'Создать категорию'},
        {'url': reverse('create_user'), 'text': 'Создать пользователя'},
        {'url': reverse('add_ingredient'), 'text': 'Добавить ингредиент'},
    ]


def index(request):
    links = generate_links()
    recipes = Recipe.objects.all()
    chefs = Author.objects.all()

    return render(request, 'recipe/index.html', {'links': links, 'chefs': chefs, 'recipes': recipes})


def recipe_detail(request, recipe_id):
    links = generate_links()
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    ingredients_list = recipe.ingredients.all()
    return render(request, 'recipe/recipe.html', {'links': links, 'recipe': recipe, 'ingredients_list': ingredients_list})


def create_category(request):
    links = generate_links()
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CategoryForm()

    return render(request, 'recipe/create_category.html', {'links': links, 'form': form})


def create_user_profile(request):
    links = generate_links()
    if request.method == 'POST':
        form = AuthorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = AuthorForm()

    return render(request, 'recipe/create_user.html', {'links': links, 'form': form})


def create_recipe(request):
    links = generate_links()
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = RecipeForm()

    return render(request, 'recipe/create_recipe.html', {'links': links, 'form': form})


def add_ingredient(request):
    links = generate_links()
    if request.method == 'POST':
        form = IngredientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = IngredientForm()

    return render(request, 'recipe/add_ingredient.html', {'links': links, 'form': form})


def delete_recipe(request, recipe_id):
    if request.method == 'POST':
        recipe = get_object_or_404(Recipe, id=recipe_id)
        recipe.delete()
        return redirect('index')
    else:
        return HttpResponseBadRequest("Invalid request method.")


def edit_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)

    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('recipe_detail', recipe_id=recipe.id)
    else:
        form = RecipeForm(instance=recipe)

    context = {'links': links, 'form': form, 'recipe': recipe}
    return render(request, 'recipe/edit_recipe.html', context)


def author_detail(request, author_id):
    links = generate_links()
    author = get_object_or_404(Author, id=author_id)
    return render(request, 'recipe/author_detail.html', {'links': links, 'author': author})


def edit_user(request, author_id):
    author = get_object_or_404(Author, id=author_id)

    if request.method == 'POST':
        form = AuthorForm(request.POST, request.FILES, instance=author)
        if form.is_valid():
            form.save()
            return redirect('author_detail', author_id=author.id)
    else:
        form = AuthorForm(instance=author)

    context = {'links': generate_links(), 'form': form, 'author': author}
    return render(request, 'recipe/edit_user.html', context)


def delete_user(request, author_id):
    author = get_object_or_404(Author, id=author_id)

    if request.method == 'POST':
        author.delete()
        return redirect('index')
    else:
        context = {'links': generate_links(), 'author': author}
        return render(request, 'recipe/delete_user.html', context)

