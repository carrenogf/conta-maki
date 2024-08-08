from django.urls import path
from . import views
urlpatterns = [
    path('home/',views.sueldos_home.as_view(),name='sueldos_home'),
]