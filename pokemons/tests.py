from django.test import TestCase
from .models import Pokemon, Type, Ability, PokemonAbilities


class PokemonAPITestCase(TestCase):
    def setUp(self):
        electric = Type.objects.create(name="electric")
        fire = Type.objects.create(name="fire")

        static = Ability.objects.create(name="static", effect="paralyzes")
        blaze = Ability.objects.create(name="blaze", effect="powers up")

        self.pikachu = Pokemon.objects.create(
            name="Pikachu", weight=60, image_url="http://example.com/pikachu.jpg"
        )
        self.pikachu.types.add(electric)
        PokemonAbilities.objects.create(pokemon=self.pikachu, ability=static)

        self.charmander = Pokemon.objects.create(
            name="Charmander", weight=85, image_url="http://example.com/charmander.jpg"
        )
        self.charmander.types.add(fire)
        PokemonAbilities.objects.create(pokemon=self.charmander, ability=blaze)

    def test_list_pokemons(self):
        response = self.client.get("/api/pokemons/")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(len(data), 2)
        names = {p["name"] for p in data}
        self.assertIn(self.pikachu.name, names)
        self.assertIn(self.charmander.name, names)

    def test_search_by_name(self):
        response = self.client.get("/api/pokemons/", {"search": self.pikachu.name})
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]["name"], self.pikachu.name)

    def test_search_by_id(self):
        response = self.client.get("/api/pokemons/", {"search": str(self.charmander.id)})
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data["name"], self.charmander.name)
