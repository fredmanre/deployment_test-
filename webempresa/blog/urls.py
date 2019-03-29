from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog, name='blog'),
    path('category/<int:id_category>', views.category, name='category')
]