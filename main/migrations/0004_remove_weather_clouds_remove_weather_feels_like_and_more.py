# Generated by Django 4.2.7 on 2024-02-26 07:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_weather_lat'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='weather',
            name='clouds',
        ),
        migrations.RemoveField(
            model_name='weather',
            name='feels_like',
        ),
        migrations.RemoveField(
            model_name='weather',
            name='sunrise',
        ),
        migrations.RemoveField(
            model_name='weather',
            name='sunset',
        ),
        migrations.RemoveField(
            model_name='weather',
            name='temp_max',
        ),
        migrations.RemoveField(
            model_name='weather',
            name='temp_min',
        ),
        migrations.RemoveField(
            model_name='weather',
            name='wind_deg',
        ),
        migrations.RemoveField(
            model_name='weather',
            name='wind_speed',
        ),
    ]
