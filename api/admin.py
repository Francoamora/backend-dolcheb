from django.contrib import admin
from .models import Producto, Evento, SiteSettings


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'categoria', 'offset')
    search_fields = ('nombre', 'categoria')


@admin.register(Evento)
class EventoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'categoria')
    search_fields = ('titulo', 'categoria')


@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        # Solo puede existir un registro
        return not SiteSettings.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False
