from django.contrib import admin
from core.models import *


# Register your models here.
@admin.register(Coffee)
class CoffeeAdmin(admin.ModelAdmin):
    list_display = ('id', 'country', 'roasting', 'mill', 'weight')


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')


@admin.register(Prices)
class PricesAdmin(admin.ModelAdmin):
    list_display = ('id', 'price')


@admin.register(Images)
class ImagesAdmin(admin.ModelAdmin):
    list_display = ('id', 'image')
