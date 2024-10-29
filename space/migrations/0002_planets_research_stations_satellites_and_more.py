# Generated by Django 4.0.4 on 2022-05-20 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('space', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Planets',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(verbose_name='Название планеты')),
                ('mass', models.FloatField(verbose_name='Масса')),
            ],
            options={
                'verbose_name': 'Планета',
                'verbose_name_plural': 'Планеты',
            },
        ),
        migrations.CreateModel(
            name='Research_stations',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(verbose_name='Название спутника')),
                ('planet_name', models.TextField(verbose_name='Название планеты, которой принадежит станция')),
                ('satellite_name', models.TextField(verbose_name='Название спутника, которому принадежит станция')),
            ],
            options={
                'verbose_name': 'Исследовательская станция',
                'verbose_name_plural': 'Исследовательские станции',
            },
        ),
        migrations.CreateModel(
            name='Satellites',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(verbose_name='Название спутника')),
                ('mass', models.FloatField(verbose_name='Масса')),
                ('planet_name', models.TextField(verbose_name='Название планеты, которой принадежит спутник')),
            ],
            options={
                'verbose_name': 'Спутник',
                'verbose_name_plural': 'Спутники',
            },
        ),
        migrations.AlterModelOptions(
            name='space',
            options={'verbose_name': 'Пост', 'verbose_name_plural': 'Посты'},
        ),
    ]
