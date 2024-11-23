from django.db import models

class Type(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Ability(models.Model):
    name = models.CharField(max_length=100)
    effect = models.CharField(max_length=255, null=False, default='No effect')
    
    def __str__(self):
        return self.name

class Pokemon(models.Model):
    name = models.CharField(max_length=100)
    weight = models.IntegerField()
    image_url = models.URLField()
    types = models.ManyToManyField(Type, related_name='pokemons')
    abilities = models.ManyToManyField(Ability, related_name='pokemons', through='PokemonAbilities')

    def __str__(self):
        return self.name

class PokemonAbilities(models.Model):
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)
    ability = models.ForeignKey(Ability, on_delete=models.CASCADE)
