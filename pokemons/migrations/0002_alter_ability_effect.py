# Generated by Django 5.1.3 on 2024-11-28 01:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemons', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ability',
            name='effect',
            field=models.CharField(default='No effect', max_length=510),
        ),
    ]