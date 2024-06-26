# Generated by Django 4.2.7 on 2024-02-26 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_remove_weather_clouds_remove_weather_feels_like_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weather',
            name='country_code',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='weather',
            name='humidity',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='weather',
            name='lat',
            field=models.CharField(default='234343433', max_length=30),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='weather',
            name='lon',
            field=models.CharField(default='232323', max_length=30),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='weather',
            name='pressure',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='weather',
            name='temperature',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='weather',
            name='visibility',
            field=models.CharField(max_length=30),
        ),
    ]
