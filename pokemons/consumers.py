# pokemons/consumers.py
import json
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import async_to_sync
from django.core.management import call_command
import asyncio
import logging

logger = logging.getLogger(__name__)

class PokemonConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add("pokemon_updates", self.channel_name)
        await self.accept()
        logger.info("WebSocket connection established")

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard("pokemon_updates", self.channel_name)
        logger.info(f"WebSocket connection closed with code: {close_code}")

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        action = text_data_json['action']
        logger.info(f"Received action: {action}")

        if action == 'import_pokemon':
            await self.channel_layer.group_send(
                "pokemon_updates",
                {
                    'type': 'import_pokemon_status',
                    'message': 'Iniciando importacion de Pokemon...'
                }
            )
            logger.info("Starting Pokemon import")
            asyncio.create_task(self.run_import_pokemon())

    async def import_pokemon_status(self, event):
        message = event['message']
        await self.send(text_data=json.dumps({
            'message': message
        }))
        logger.info(f"Sent status update: {message}")

    async def run_import_pokemon(self):
        logger.info("Running import_pokemon command")
        try:
            await asyncio.to_thread(call_command, 'import_pokemon')
            logger.info("import_pokemon command completed successfully")
        except Exception as e:
            logger.error(f"Error running import_pokemon command: {str(e)}")
            await self.channel_layer.group_send(
                "pokemon_updates",
                {
                    'type': 'import_pokemon_status',
                    'message': f'Error en la importacion: {str(e)}'
                }
            )