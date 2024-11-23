from rest_framework.routers import DefaultRouter
from .views import PokemonViewSet
from django.urls import path, include
from .views import ImportPokemonView
from django.conf.urls.static import static
from django.conf import settings

router = DefaultRouter()
router.register(r'pokemons', PokemonViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('import-pokemon/', ImportPokemonView.as_view(), name='import_pokemon'),
]

if not settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)