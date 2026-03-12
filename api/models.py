from django.db import models

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