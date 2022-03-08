from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from agenda.models import eventos

# Create your views here.

def index(request):
    return HttpResponse("Olá Mundo!")

def exibir_evento(request):
    evento = eventos[0]
    # template = loader.get_template("agenda/exibir_eventos.html")
    # rendered_template = template.render(context={"evento": evento}, request=request)
    # return HttpResponse(rendered_template)
    return render(request=request, context={"evento": evento}, template_name="agenda/exibir_eventos.html")
