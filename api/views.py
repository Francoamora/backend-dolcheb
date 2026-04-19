from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .models import Producto, Evento, SiteSettings
from .serializers import ProductoSerializer, EventoSerializer, SiteSettingsSerializer


class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer


class EventoViewSet(viewsets.ModelViewSet):
    queryset = Evento.objects.all()
    serializer_class = EventoSerializer


class SiteSettingsView(APIView):
    """
    GET  /api/settings/ → devuelve la configuración (sin auth)
    PATCH /api/settings/ → actualiza la configuración (requiere auth por la autenticación global)
    """

    def get_permissions(self):
        if self.request.method == 'GET':
            return [AllowAny()]
        return super().get_permissions()

    def get_object(self):
        obj, _ = SiteSettings.objects.get_or_create(pk=1)
        return obj

    def get(self, request):
        settings = self.get_object()
        serializer = SiteSettingsSerializer(settings, context={'request': request})
        return Response(serializer.data)

    def patch(self, request):
        settings = self.get_object()
        serializer = SiteSettingsSerializer(
            settings, data=request.data, partial=True, context={'request': request}
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
