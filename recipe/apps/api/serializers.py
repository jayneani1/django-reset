from rest_framework import serializers
from apps.api.models import (
    Category, Recipe
)
class RecipeSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Recipe
        fields = ('id', 'name', 'description',
                  'owner', 'category',
                  'ingredients', 'directions',
                  'created_at', 'updated_at',
                  'is_public')
class CategorySerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    recipes = RecipeSerializer(many=True, read_only=True, required=False)
    class Meta:
        model = Category
        fields = ('id', 'name', 'owner',
                  'description', 'recipes',
                  'created_at', 'updated_at')