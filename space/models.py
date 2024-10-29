from tabnanny import verbose
from turtle import title
from django.db import models

# Create your models here.

class Space(models.Model):
    title = models.CharField(max_length=170, verbose_name='Заголовок')
    content = models.TextField(verbose_name='Сообщение')
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True, verbose_name='Дата')
    updated = models.DateTimeField(auto_now=True, auto_now_add=False, verbose_name='Дата обновления')
    
    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

class Planets(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name='ID')
    name = models.TextField(verbose_name='Название планеты')
    mass = models.FloatField(verbose_name='Масса')
    
    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Планета'
        verbose_name_plural = 'Планеты'

class Satellites(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name='ID')
    name = models.TextField(verbose_name='Название спутника')
    mass = models.FloatField(verbose_name='Масса')
    planet_name = models.TextField(verbose_name='Название планеты, которой принадежит спутник')
    
    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Спутник'
        verbose_name_plural = 'Спутники'

class Research_stations(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name='ID')
    name = models.TextField(verbose_name='Название станции')
    planet_name = models.TextField(verbose_name='Название планеты, которой принадежит станция')
    satellite_name = models.TextField(verbose_name='Название спутника, которому принадежит станция')
    
    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Исследовательская станция'
        verbose_name_plural = 'Исследовательские станции'