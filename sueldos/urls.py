from django.urls import path
from . import views
urlpatterns = [
    path('liquidaciones/',views.liquidaciones_list,name='liquidaciones'),
]