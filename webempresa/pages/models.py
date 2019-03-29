from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Page(models.Model):
    title = models.CharField('nombre', max_length=100, unique=True)
    content = RichTextField("contenido")
    order = models.SmallIntegerField("orden", default=0)
    created = models.DateTimeField("fecha de creacion", auto_now_add=True)
    updated = models.DateTimeField("fecha de modificacion", auto_now=True)

    class Meta:
        verbose_name = 'página'
        verbose_name_plural = 'páginas'
        ordering = ['order', 'title']

    def __str__(self):
        return self.title
    