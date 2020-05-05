from django.conf.urls import url
from rest_framework.routers import DefaultRouter
from .views import (
    CategoryViewSet, CategoryRecipes,
    SingleCategoryRecipe, RecipesViewSet
)
router = DefaultRouter()
router.register('categories', CategoryViewSet, basename='categories')
router.register('recipes', RecipesViewSet, basename='recipes')
custom_urlpatterns = [
    url(r'categories/(?P<category_pk>\d+)/recipes$', CategoryRecipes.as_view(), name='category_recipes'),
    url(r'categories/(?P<category_pk>\d+)/recipes/(?P<pk>\d+)$', SingleCategoryRecipe.as_view(),
        name='single_category_recipe')
]
urlpatterns = router.urls
urlpatterns += custom_urlpatterns