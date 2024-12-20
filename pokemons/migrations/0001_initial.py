# Generated by Django 5.1.3 on 2024-11-21 05:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ability',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('effect', models.CharField(default='No effect', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Pokemon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('weight', models.IntegerField()),
                ('image_url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='PokemonAbilities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ability', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pokemons.ability')),
                ('pokemon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pokemons.pokemon')),
            ],
        ),
        migrations.AddField(
            model_name='pokemon',
            name='abilities',
            field=models.ManyToManyField(related_name='pokemons', through='pokemons.PokemonAbilities', to='pokemons.ability'),
        ),
        migrations.AddField(
            model_name='pokemon',
            name='types',
            field=models.ManyToManyField(related_name='pokemons', to='pokemons.type'),
        ),
    ]
