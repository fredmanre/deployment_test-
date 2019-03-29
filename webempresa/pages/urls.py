from django.urls import path
from . import views

# se debe colocar el slug cuando haces el llmaado para el ceo e un enlace(aviso legal)
urlpatterns = [
    path('<int:page_id>/<slug:page_slug>/', views.page, name='page'),
]