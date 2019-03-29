from django.db import models

# Create your models here.
class Social(models.Model):
    key = models.SlugField(("nombre clave"), max_length=100, unique=True)
    name = models.CharField(("Red social"), max_length=200)
    url = models.URLField(verbose_name="Enlace", max_length=200, blank=True, null=True)
    created = models.DateTimeField("fecha de creacion", auto_now_add=True)
    updated = models.DateTimeField("fecha de modificacion", auto_now=True)

    class Meta:
        verbose_name = 'enlace'
        verbose_name_plural = 'enlaces'
        ordering = ['-name']

    def __str__(self):
        return self.name
    