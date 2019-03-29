from .models import Social

# procesador de contexto, es una funcion que se puede ejecutar en todo el codigo
def ctx_dict(request):
    ctx = {}
    links = Social.objects.all()
    for link in links:
        ctx[link.key] = link.url
    return ctx