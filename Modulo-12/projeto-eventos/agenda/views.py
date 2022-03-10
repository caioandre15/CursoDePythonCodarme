from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.template import loader
from datetime import date

from agenda.models import Evento

# Create your views here.

def listar_eventos(request):
    # Buscar os nossos eventos criados no banco
    eventos = Evento.objects.filter(data__gte=date.today()).order_by('data')
    # Exibir um template listando esses eventos    
    return render(
        request=request, 
        context={"eventos": eventos}, 
        template_name="agenda/listar_eventos.html"
    )
    

def exibir_evento(request, id):
    evento = get_object_or_404(Evento, id=id)
    evento = Evento.objects.get(id=id) #Get() vai tentar buscar apenas um elemento
    # template = loader.get_template("agenda/exibir_eventos.html")
    # rendered_template = template.render(context={"evento": evento}, request=request)
    # return HttpResponse(rendered_template)
    return render(
        request=request, 
        context={"evento": evento}, 
        template_name="agenda/exibir_eventos.html"
    )
