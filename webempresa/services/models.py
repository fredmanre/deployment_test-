from django.db import models

# Create your models here.

class Service(models.Model):
    title = models.CharField("titulo", max_length=200)
    subtitle = models.CharField('subtitulo', max_length=200)
    content = models.TextField('contenido')
    image = models.ImageField('imagen', upload_to='services')
    created = models.DateTimeField("fecha de creacion", auto_now_add=True)
    updated = models.DateTimeField("fecha de actualizacion", auto_now=True)

    class Meta:
        verbose_name = "servicio"
        verbose_name_plural = "servicios"
        ordering = ['-created']

    def __str__(self):
        return self.title

