from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
from .views import recipe_detail

urlpatterns = [
    path('', views.index, name='index'),
    path('create_category/', views.create_category, name='create_category'),
    path('create_user/', views.create_user_profile, name='create_user'),
    path('create_recipe/', views.create_recipe, name='create_recipe'),
    path('add_ingredient/', views.add_ingredient, name='add_ingredient'),
    path('recipe_detail/<int:recipe_id>/', recipe_detail, name='recipe_detail'),
    path('delete_recipe/<int:recipe_id>/', views.delete_recipe, name='delete_recipe'),
    path('edit_recipe/<int:recipe_id>/', views.edit_recipe, name='edit_recipe'),
    path('author_detail/<int:author_id>/', views.author_detail, name='author_detail'),
    path('edit_user/<int:author_id>/', views.edit_user, name='edit_user'),
    path('delete_user/<int:author_id>/', views.delete_user, name='delete_user'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
