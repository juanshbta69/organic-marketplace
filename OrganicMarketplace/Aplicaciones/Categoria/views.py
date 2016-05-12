from django.shortcuts import render
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
import json
# Create your views here.
from OrganicMarketplace.Aplicaciones.Categoria.models import Categoria


@csrf_exempt
def getCategoria(request,categoria_id):
    if request.method == 'GET':
        categoria = Categoria.objects.get(pk=categoria_id)
        return HttpResponse(serializers.serialize("json",[categoria]))

@csrf_exempt
def gestionCategoria(request):
    if request.method == 'GET':
        categorias = Categoria.objects.all()
        return HttpResponse(serializers.serialize("json",categorias))
    if request.method == 'POST':
        jsonData = json.loads(request.body)
        categoria = Categoria()
        categoria.nombre = jsonData['nombre']
        categoria.descripcion = jsonData['descripcion']
        categoria.save()
        return HttpResponse(serializers.serialize("json", [categoria]))
    if request.method == 'PUT':
        jsonData = json.loads(request.body)
        categoria = Categoria.objects.get(id=jsonData['pk'])
        categoria.nombre = jsonData['nombre']
        categoria.descripcion = jsonData['descripcion']
        categoria.save()
        return HttpResponse(serializers.serialize("json",{categoria}))
    if request.method == 'DELETE':
        jsonData = json.loads(request.body)
        categoria = Categoria.objects.get(id=jsonData['pk'])
        categoria.delete()
        return JsonResponse({"mensaje": "ok"})