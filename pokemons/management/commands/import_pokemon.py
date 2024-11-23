from django.core.management.base import BaseCommand
from django.db import transaction
from asgiref.sync import sync_to_async
from pokemons.models import Pokemon, Type, Ability, PokemonAbilities
import aiohttp
import asyncio
import time
from channels.layers import get_channel_layer

class Command(BaseCommand):
    help = 'fetch Pokemon data from PokeAPI'
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.channel_layer = get_channel_layer()

    async def send_update(self, message):
        await self.channel_layer.group_send(
            "pokemon_updates",
            {
                "type": "import_pokemon_status",
                "message": message
            }
        )

    async def fetch_data(self, session, url):
        async with session.get(url) as response:
            return await response.json()

    @sync_to_async
    def create_or_update_pokemon(self, details):
        with transaction.atomic():
            pokemon, created = Pokemon.objects.update_or_create(
                id=details['id'],
                defaults={
                    'name': details['name'],
                    'weight': details['weight'],
                    'image_url': details['sprites']['front_default'],
                }
            )
            pokemon.types.clear()
            PokemonAbilities.objects.filter(pokemon=pokemon).delete()
            return pokemon

    @sync_to_async
    def process_types(self, pokemon, types):
        for type_info in types:
            type_name = type_info['type']['name']
            type_obj, _ = Type.objects.get_or_create(name=type_name)
            pokemon.types.add(type_obj)

    @sync_to_async
    def process_abilities(self, pokemon, abilities):
        for ability_info in abilities:
            ability, _ = Ability.objects.get_or_create(
                name=ability_info['name'],
                defaults={'effect': ability_info['effect']}
            )
            PokemonAbilities.objects.create(pokemon=pokemon, ability=ability)

    async def process_pokemon(self, session, url):
        # print('Iniciando proceso de pokemon')
        # print('aca2')
        details = await self.fetch_data(session, url)
        pokemon = await self.create_or_update_pokemon(details)
        await self.process_types(pokemon, details['types'])

        ability_tasks = []
        for ability_info in details['abilities']:
            ability_url = ability_info['ability']['url']
            ability_tasks.append(self.fetch_data(session, ability_url))
        ability_details = await asyncio.gather(*ability_tasks)

        abilities_data = []
        for ability_detail in ability_details:
            effect = next((entry['effect'] for entry in ability_detail['effect_entries'] 
                           if entry['language']['name'] == 'en'), '')
            abilities_data.append({
                'name': ability_detail['name'],
                'effect': effect[:255] if effect else 'No effect'
            })

        await self.process_abilities(pokemon, abilities_data)
        self.stdout.write(f"Pokemon procesado: {pokemon.name} (ID: {pokemon.id})")

    async def handle_async(self, *args, **options):
        start_time = time.time()
        await self.send_update("Tarea de Pokemon iniciada!")
        
        base_url = 'https://pokeapi.co/api/v2/pokemon'
        async with aiohttp.ClientSession() as session:
            pokemon_tasks = []
            for i in range(2):
                url = f'{base_url}?offset={i*20}&limit=20'
                response = await self.fetch_data(session, url)
                total_pokemon = len(response['results'])
                for index, pokemon_data in enumerate(response['results']):
                    pokemon_tasks.append(self.process_pokemon(session, pokemon_data['url']))
                    if (index + 1) % 10 == 0 or index + 1 == total_pokemon:
                        await self.send_update(f"Procesando Pokemon {index + 1} de {total_pokemon}")
            await asyncio.gather(*pokemon_tasks)

        end_time = time.time()
        duration = end_time - start_time
        await self.send_update(f"Tarea completada en {duration:.2f} segundos.")

    def handle(self, *args, **options):
        # print('aca iniciado')
        asyncio.run(self.handle_async(*args, **options))