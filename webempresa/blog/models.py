from django.db import models
from django.utils.timezone import now
# modelo de usuario de django
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField('nombre', max_length=100)
    created = models.DateTimeField("fecha de creacion", auto_now_add=True)
    updated = models.DateTimeField("fecha de actualizacion", auto_now=True)

    class Meta:
        verbose_name = "categoria"
        verbose_name_plural = "categorias"
        ordering = ['-created']

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField('titulo', max_length=200)
    content = models.TextField('contenido')
    published = models.DateTimeField('Fecha de publicacion', default=now)
    image = models.ImageField('imagen', upload_to='blog', null=True, blank=True)
    author = models.ForeignKey(User, verbose_name="Autor", on_delete=models.CASCADE)
    # el related name permite darle un nombre a un objeto relacionado, util a la hora de usarlo
    category = models.ManyToManyField(Category, verbose_name='categorias', related_name="get_posts")
    created = models.DateTimeField("fecha de creacion", auto_now_add=True)
    updated = models.DateTimeField("fecha de actualizacion", auto_now=True)

    class Meta:
        verbose_name = "entrada"
        verbose_name_plural = "entradas"
        ordering = ['-created']

    def __str__(self):
        return self.title
