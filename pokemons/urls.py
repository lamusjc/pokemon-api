from rest_framework.routers import DefaultRouter
from .views import PokemonViewSet
from django.urls import path, include
from .views import ImportPokemonView

router = DefaultRouter()
router.register(r'pokemons', PokemonViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('import-pokemon/', ImportPokemonView.as_view(), name='import_pokemon'),
]