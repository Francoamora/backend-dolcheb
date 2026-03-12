from django.contrib import admin
from .models import Producto, Evento

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'categoria', 'offset')
    search_fields = ('nombre', 'categoria')

@admin.register(Evento)
class EventoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'categoria')
    search_fields = ('titulo', 'categoria')