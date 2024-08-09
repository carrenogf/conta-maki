from django.urls import path
from . import views
urlpatterns = [
    path('home/',views.sueldos_home.as_view(),name='sueldos_home'),
    path('recibo-liquidacion/<int:liquidacion>/',views.recibo_seleccionar_empleado,name='recibo_liquidacion'),
]