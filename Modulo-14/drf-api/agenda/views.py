import email
from functools import partial
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view

from agenda.models import Agendamento
from agenda.serializers import AgendamentoSerializer
from rest_framework.response import Response
# Create your views here.


@api_view(http_method_names=["GET", "PATCH", "DELETE"])
def agendamento_detail(request, id):
    if request.method == "GET":
        obj = get_object_or_404(Agendamento, id=id)
        serializer = AgendamentoSerializer(obj)
        return JsonResponse(serializer.data)
    if request.method == "PATCH":
        obj = get_object_or_404(Agendamento, id=id)
        serializer = AgendamentoSerializer(data=request.data, partial=True)
        if serializer.is_valid():
            validated_date = serializer.validated_data
            obj.data_horario = validated_date.get("data_horario", obj.data_horario)
            obj.nome_cliente = validated_date.get("nome_cliente", obj.nome_cliente)
            obj.email_cliente = validated_date.get("email_cliente", obj.email_cliente)
            obj.telefone_cliente = validated_date.get("telefone_cliente", obj.telefone_cliente)
            obj.save()
            return JsonResponse(validated_date, status=200)
        return JsonResponse(serializer.errors, status=400)
    if request.method == "DELETE":
        obj = get_object_or_404(Agendamento, id=id)
        obj.delete()
        return Response(status=204)


@api_view(http_method_names=["GET", "POST"])
def agendamento_list(request):
    if request.method == "GET":
        qs = Agendamento.objects.all()
        serializer = AgendamentoSerializer(qs, many=True)
        return JsonResponse(serializer.data, safe=False)
    if request.method == "POST":
        data = request.data  # {"nome_cliente": "Gabriel"}...
        serializer = AgendamentoSerializer(data=data)
        if serializer.is_valid():
            validated_data = serializer.validated_data
            Agendamento.objects.create(
                data_horario=validated_data["data_horario"],
                nome_cliente=validated_data["nome_cliente"],
                email_cliente=validated_data["email_cliente"],
                telefone_cliente=validated_data["telefone_cliente"]
            )
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
