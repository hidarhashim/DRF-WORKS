from recipes.models import Recipe

from rest_framework import serializers


class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Recipe
        fields='__all__'

        read_only_fields=['id','created']