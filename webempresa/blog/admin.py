from django.contrib import admin
from .models import Category, Post

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')


class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    # lista en el panel
    list_display = ('title', 'author', 'published', 'post_category')
    # para el orden
    ordering = ('author', 'published')
    # filtro para busquedas, tomar en cuenta el guion bajo para campos especiales
    search_fields = ('title', 'content', 'author__username', 'category__name')
    # para ordenanr y buscar por fechas(muchas entradas)
    date_hierarchy = ('published')
    # filtro para busquedas
    list_filter = ('author__username', 'category__name')

    # crear etiquetas para tablas propias
    def post_category(self, obj):
        return ", ".join([c.name for c in obj.category.all().order_by('name')])
    # con esto cambiamos el nombre a mostrar en el panel a categorias y no al nombre de la func
    post_category.short_description = 'categorias'


admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)