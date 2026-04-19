from rest_framework import serializers
from .models import Producto, Evento, SiteSettings


class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'


class EventoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evento
        fields = '__all__'


class SiteSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SiteSettings
        fields = '__all__'
