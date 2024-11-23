import threading
from django.shortcuts import get_object_or_404, render
from rest_framework import viewsets
from rest_framework.views import APIView
from .models import Pokemon
from .serializers import PokemonSerializer
from asgiref.sync import async_to_sync
from rest_framework.response import Response
from channels.layers import get_channel_layer
from django.core.management import call_command

class PokemonViewSet(viewsets.ModelViewSet):
    queryset = Pokemon.objects.all().order_by('id')
    serializer_class = PokemonSerializer
    
    def list(self, request):
        search_param = request.query_params.get('search', None)
        if search_param:
            try:
                pokemon_id = int(search_param)
                pokemon = get_object_or_404(Pokemon, id=pokemon_id)
                serializer = self.get_serializer(pokemon)
                return Response(serializer.data)
            except ValueError:
                queryset = self.queryset.filter(name__icontains=search_param)
        else:
            queryset = self.queryset

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        try:
            pokemon_id = int(pk)
            pokemon = get_object_or_404(Pokemon, id=pokemon_id)
        except ValueError:
            pokemon = get_object_or_404(Pokemon, name__iexact=pk)

        serializer = self.get_serializer(pokemon)
        return Response(serializer.data)
    
class ImportPokemonView(APIView):
    def post(self, request):
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            "pokemon_updates",
            {
                "type": "import_pokemon_status",
                "message": "Iniciando importacion desde API"
            }
        )
        
        thread = threading.Thread(target=self.run_import)
        thread.start()
        
        return Response({"status": "Import started"})

    def run_import(self):
        try:
            call_command('import_pokemon')
        except Exception as e:
            channel_layer = get_channel_layer()
            async_to_sync(channel_layer.group_send)(
                "pokemon_updates",
                {
                    "type": "import_pokemon_status",
                    "message": f"Error durante la importacion: {str(e)}"
                }
            )
