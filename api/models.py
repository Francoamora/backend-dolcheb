from django.db import models


class SiteSettings(models.Model):
    """Singleton — siempre pk=1. Permite cambiar la imagen de la cascada desde el admin."""
    cascada_img = models.ImageField(upload_to='site/', null=True, blank=True,
                                    help_text="Imagen de la cascada de chocolate (galería principal)")

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        pass  # No se puede borrar el singleton

    class Meta:
        verbose_name = "Configuración del Sitio"
        verbose_name_plural = "Configuración del Sitio"

    def __str__(self):
        return "Configuración del Sitio"


class Producto(models.Model):
    nombre = models.CharField(max_length=150)
    descripcion = models.TextField()
    categoria = models.CharField(max_length=50) # Ej: Tortas, Tartas, Bocados
    img = models.ImageField(upload_to='productos/')
    # Este campo nos sirve para hacer el diseño asimétrico en Next.js que tanto nos gustó
    offset = models.BooleanField(default=False, help_text="Marcar para empujar la tarjeta hacia abajo en el diseño web")

    def __str__(self):
        return self.nombre

class Evento(models.Model):
    titulo = models.CharField(max_length=150)
    categoria = models.CharField(max_length=50) # Ej: Bodas, Cumpleaños, Cascada
    img = models.ImageField(upload_to='eventos/')

    def __str__(self):
        return self.titulo