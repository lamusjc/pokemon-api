from django.contrib import admin
from .models import Pokemon, Ability, Type, PokemonAbilities

class TypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

class AbilityAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'effect') 

class PokemonAbilitiesInline(admin.TabularInline):
    model = PokemonAbilities
    extra = 1

class PokemonAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'weight', 'image_url')
    search_fields = ['name']
    raw_id_fields = ('types', 'abilities') 
    inlines = [PokemonAbilitiesInline]

admin.site.register(Pokemon, PokemonAdmin)
admin.site.register(Type, TypeAdmin)
admin.site.register(Ability, AbilityAdmin)
admin.site.register(PokemonAbilities)
