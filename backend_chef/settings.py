"""
Django settings for backend_chef project.
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-a3x8a7l#hr2-!7*#-ld08&fpnac#cgq$-(&jf(g1)d^@c)#jz^'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'jazzmin', # <--- ¡MAGIA! Siempre primero.
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # --- NUESTRAS APPS Y LIBRERÍAS ---
    'rest_framework',
    'corsheaders',
    'api',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware', # <-- CORS agregado acá, muy importante
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'backend_chef.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'backend_chef.wsgi.application'

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
LANGUAGE_CODE = 'es-ar'
TIME_ZONE = 'America/Argentina/Buenos_Aires'
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = 'static/'

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# --- CONFIGURACIONES PRO PARA NEXT.JS ---

# Permiso para que Next.js pueda pedir datos
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://localhost:3001",
    "https://dolcheb.com.ar",
    "https://www.dolcheb.com.ar",
    "https://proyecto-chef.vercel.app",
]

# Configuración para guardar y servir las fotos que suba el Chef
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# =========================================================
# CONFIGURACIÓN PREMIUM DEL PANEL (DJANGO JAZZMIN)
# =========================================================
JAZZMIN_SETTINGS = {
    # Títulos y nombres
    "site_title": "Dolche'B Admin",
    "site_header": "Dolche'B",
    "site_brand": "Panel del Chef",
    
    # Texto de bienvenida
    "welcome_sign": "Bienvenido al sistema de gestión de Dolche'B",
    
    # Copyright del footer
    "copyright": "Desarrollado por Franco Mora",
    
    # Ocultar cositas que no sirven
    "search_model": [],
    "user_avatar": None,
    
    # Botón mágico arriba para ir a tu Frontend en Next.js
    "topmenu_links": [
        {"name": "Inicio",  "url": "admin:index", "permissions": ["auth.view_user"]},
        {"name": "Ver Sitio Web", "url": "http://localhost:3000", "new_window": True},
    ],
    
    # Menú lateral
    "show_sidebar": True,
    "navigation_expanded": True,
    
    # Íconos de FontAwesome para tus modelos
    "icons": {
        "auth": "fas fa-users-cog",
        "auth.user": "fas fa-user",
        "auth.Group": "fas fa-users",
        "api.Producto": "fas fa-birthday-cake", # Ícono de torta para los productos
        "api.Evento": "fas fa-camera",          # Ícono de cámara para los eventos
    },
    
    "default_icon_parents": "fas fa-chevron-circle-right",
    "default_icon_children": "fas fa-circle",
}

# Diseño: Oscuro y elegante para que combine con el frontend
JAZZMIN_UI_TWEAKS = {
    "theme": "darkly",
    "dark_mode_theme": "darkly",
    "navbar": "navbar-dark",
    "sidebar": "sidebar-dark-danger", # Acentos en ROJO Dolche'B
    "accent": "accent-danger",
    "button_classes": {
        "primary": "btn-danger",
        "secondary": "btn-outline-light",
        "info": "btn-info",
        "warning": "btn-warning",
        "danger": "btn-danger",
        "success": "btn-success"
    }
}