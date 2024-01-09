# forms.py
from django import forms
from ..models import Recipe, Ingredient


class RecipeForm(forms.ModelForm):
    ingredients = forms.ModelMultipleChoiceField(
        queryset=Ingredient.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )

    class Meta:
        model = Recipe
        fields = ['title', 'description', 'ingredients', 'directions', 'image', 'author', 'category']

    directions = forms.CharField(
        label="Ход приготовления",
        widget=forms.Textarea(attrs={'cols': 80, 'rows': 20})
    )
