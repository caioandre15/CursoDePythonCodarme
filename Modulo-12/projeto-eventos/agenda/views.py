from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.template import loader
from datetime import date
from django.urls import reverse

from agenda.models import Evento, Categoria

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

def participar_evento(request):
    evento_id = request.POST.get("evento_id")
    evento = get_object_or_404(Evento, id=evento_id)
    evento.participantes += 1
    evento.save()
    
    return HttpResponseRedirect(reverse('exibir_evento', args=(evento_id,)))

def listar_categorias(request):
    # Buscar os nossos eventos criados no banco
    categorias = Categoria.objects.all()
    # Exibir um template listando esses eventos    
    return render(
        request=request, 
        context={"categorias": categorias}, 
        template_name="agenda/listar_categorias.html"
    )

def exibir_categoria(request, id):
    categoria = get_object_or_404(Categoria, id=id)
    categoria = Categoria.objects.get(id=id)
    qtde_categoria = Evento.objects.filter(categoria__id=id, data__gte=date.today()).count()
    return render(
        request=request, 
        context={"categoria": categoria, "qtde_categoria": qtde_categoria}, 
        template_name="agenda/exibir_categoria.html"
    )