from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path("", views.saverecords),
    path('minha_consulta', views.saverecords, name='minha_consulta')
]