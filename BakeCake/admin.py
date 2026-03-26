from django.contrib import admin
from .models import (
    OrderedCake,
    Order,
    Cake,
    Client,
    Layer,
    Shape,
    Topping,
    Berry,
    Inscription,
    Decor
)


@admin.register(OrderedCake)
class OrderedCakeAdmin(admin.ModelAdmin):
    list_display = ['order', 'cake', 'quantity']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['client', 'order_price', 'status']
    list_filter = ['status']
    list_editable = ['status']


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['fio', 'phone', 'address']


@admin.register(Cake)
class CakeAdmin(admin.ModelAdmin):
    list_display = ['picture', 'title']
    list_display_links = ['picture', 'title']


@admin.register(Layer)
class LayerAdmin(admin.ModelAdmin):
    list_display = ['quantity', 'price']


@admin.register(Shape)
class ShapeAdmin(admin.ModelAdmin):
    list_display = ['shape', 'price']


@admin.register(Topping)
class ToppingAdmin(admin.ModelAdmin):
    list_display = ['title', 'price']


@admin.register(Berry)
class BerryAdmin(admin.ModelAdmin):
    list_display = ['title', 'price']


@admin.register(Inscription)
class InscriptionAdmin(admin.ModelAdmin):
    list_display = ['title', 'price']


@admin.register(Decor)
class DecorAdmin(admin.ModelAdmin):
    list_display = ['title', 'price']
