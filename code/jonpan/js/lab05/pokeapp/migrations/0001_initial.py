# Generated by Django 4.1 on 2022-09-30 03:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PokemonType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Pokemon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('name', models.CharField(max_length=200)),
                ('height', models.FloatField()),
                ('weight', models.FloatField()),
                ('image_front', models.CharField(max_length=100)),
                ('image_back', models.CharField(max_length=100)),
                ('types', models.ManyToManyField(blank=True, related_name='pokemon', to='pokeapp.pokemontype')),
            ],
        ),
    ]
