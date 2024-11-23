from rest_framework import serializers
from .models import Pokemon, Type, Ability

class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = ['id', 'name']

class AbilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Ability
        fields = ['id', 'name', 'effect']

class PokemonSerializer(serializers.ModelSerializer):
    types = TypeSerializer(many=True) 
    abilities = AbilitySerializer(many=True)

    class Meta:
        model = Pokemon
        fields = ['id', 'name', 'weight', 'image_url', 'types', 'abilities']
