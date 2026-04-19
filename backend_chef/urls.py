from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from api.views import ProductoViewSet, EventoViewSet, SiteSettingsView
from django.conf import settings
from django.conf.urls.static import static

# Acá creamos las rutas de tu API automáticamente
router = DefaultRouter()
router.register(r'productos', ProductoViewSet)
router.register(r'eventos', EventoViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/settings/', SiteSettingsView.as_view(), name='site_settings'),
]

# Esto es CLAVE para que Next.js pueda cargar las fotos que subas
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
