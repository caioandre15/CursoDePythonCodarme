from django.urls import URLPattern
from django.urls import path
from agenda.views import listar_eventos, exibir_evento

urlpatterns = [
    path("", listar_eventos),
    path("evento", exibir_evento)
]