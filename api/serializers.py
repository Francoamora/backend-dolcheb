from rest_framework import serializers
from .models import Producto, Evento

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__' # Esto agarra todos los campos que creaste (nombre, img, offset, etc.)

class EventoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evento
        fields = '__all__'