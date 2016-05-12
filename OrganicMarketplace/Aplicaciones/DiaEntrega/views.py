import json

from django.core import serializers
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from models import User
from .models import DiaEntrega


# Create your views here.
@csrf_exempt
def dias_entrega(request):
    if request.method == 'GET':
        dias_entrega = DiaEntrega.objects.all().values('pk', 'diaSemana', 'numDia')
        dias_entrega = json.loads(json.dumps(list(dias_entrega)))
        return JsonResponse(dias_entrega, safe=False)


@csrf_exempt
def definir_dias_entrega(request):
    DiaEntrega.objects.all().delete()
    json_dias_entrega = json.loads(request.body)
    if request.method == 'POST':
        if json_dias_entrega is not None:
            dias_entrega = json_dias_entrega['diasEntrega']

            print 'Numero de dias seleccionados: ' + str(len(dias_entrega))

            for dia in dias_entrega:
                dia_entrega = DiaEntrega()
                usuario_id = json_dias_entrega['administradorId']
                usuario = User.objects.get(pk=usuario_id)

                dia_entrega.numDia = dia['numDia']
                dia_entrega.diaSemana = dia['diaSemana']
                dia_entrega.usuarioId = usuario
                dia_entrega.save()
                mensaje = 'ok'
        else:
            mensaje = 'error'
    else:
        mensaje = 'error'

    return JsonResponse({"mensaje": mensaje})
