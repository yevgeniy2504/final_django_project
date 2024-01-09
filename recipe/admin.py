from django.contrib import admin
from .models import Category, Author, Ingredient, Recipe


class RecipeAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Recipe Information', {
            'fields': ('title', 'description', 'ingredients', 'directions', 'image')
        }),
        ('Categorization', {
            'fields': ('category',),
        }),
        ('Author and Date', {
            'fields': ('author', 'created_at', 'updated_at'),
        }),
    )

    def get_queryset(self, request):
        return super().get_queryset(request).select_related('category', 'author')

    def category(self, obj):
        return obj.category.name

    category.admin_order_field = 'category__name'

    def author(self, obj):
        return obj.author.name

    readonly_fields = ('created_at', 'updated_at')

    list_display = ('title', 'category', 'author', 'created_at')
    list_filter = ('category', 'title')
    search_fields = ('description',)


class IngredientAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    ordering = ['name']


admin.site.register(Category)
admin.site.register(Author)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Recipe, RecipeAdmin)
