from django.contrib import admin
from .models import Social

# Register your models here.
class SocialAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

    # esto solo mostrara los campos como lectura para el tipo de usuario del grupo Personal
    def get_readonly_fields(self, request, obj=None):
        if request.user.groups.filter(name="Personal").exists():
            return ('key', 'name')
        else:
            return ('created', 'updated')


admin.site.register(Social, SocialAdmin)