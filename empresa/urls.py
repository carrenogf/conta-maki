from django.urls import path
from . import views
urlpatterns = [
    path('seleccionar_empresa/', views.seleccionar_empresa, name='seleccionar_empresa'),
]