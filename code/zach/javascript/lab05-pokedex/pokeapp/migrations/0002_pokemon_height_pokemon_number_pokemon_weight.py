# Generated by Django 4.1 on 2022-10-08 01:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokeapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pokemon',
            name='height',
            field=models.IntegerField(default=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pokemon',
            name='number',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pokemon',
            name='weight',
            field=models.IntegerField(default=10),
            preserve_default=False,
        ),
    ]
