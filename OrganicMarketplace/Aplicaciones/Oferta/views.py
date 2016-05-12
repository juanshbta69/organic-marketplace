import decimal

from django.db.models import Q
from django.db.models.base import ModelState
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from OrganicMarketplace.Aplicaciones.Productor.models import Productor_Producto
from models import Oferta
from django.core import serializers
from models import Productor
from models import Producto

import json


@csrf_exempt
def offers(request):
    if request.method == 'GET':
        oferta = Oferta.objects.all().values('productor__telefono', 'productor__descripcion', 'productor__direccion',
                                             'producto__cantidadMinima', 'producto__imagen', 'producto__descripcion',
                                             'producto__nombre', 'producto__unidadMedida', 'estado', 'total',
                                             'precioUnitario', 'cantidad', 'fecha', 'id')
        productores = json.loads(json.dumps(list(oferta), cls=DateTimeEncoder))
        return JsonResponse(productores, safe=False)
    if request.method == 'PUT':
        json_project = json.loads(request.body.decode('utf-8'))
        oferta = Oferta.objects.get(pk=json_project.get('id'))
        oferta.estado = json_project.get('estado')
        oferta.save()
        oferta = Oferta.objects.all().values('productor__telefono', 'productor__descripcion', 'productor__direccion',
                                             'producto__cantidadMinima', 'producto__imagen', 'producto__descripcion',
                                             'producto__nombre', 'producto__unidadMedida', 'estado', 'total',
                                             'precioUnitario', 'cantidad', 'fecha', 'id')
        productores = json.loads(json.dumps(list(oferta), cls=DateTimeEncoder))
        return JsonResponse(productores, safe=False)


@csrf_exempt
def create_offer(request):
    json_offer = json.loads(request.body)
    estado = "creada"
    if request.method == 'POST':
        productor = Productor.objects.filter(usuarioId_id=json_offer['user_id']).first()
        producto = Producto.objects.get(pk=json_offer['producto_pk'])
        if productor is not None and producto is not None:
            offer = Oferta()
            offer.productor = productor
            offer.producto = producto
            offer.fecha = json_offer['fecha']
            offer.cantidad = json_offer['cantidad']
            offer.precioUnitario = json_offer['precio_unitario']
            offer.total = json_offer['total']
            offer.estado = estado
            offer.save()
            return HttpResponse(serializers.serialize("json", [offer]))
        else:
            return JsonResponse({"mensaje": "error"})


@csrf_exempt
def update_offer(request):
    json_offer = json.loads(request.body)
    if request.method == 'POST':
        offer = Oferta.objects.get(pk=json_offer['id'])
        producto = Producto.objects.get(pk=json_offer['producto_pk'])
        if producto is not None:
            offer.producto = producto
            offer.cantidad = json_offer['cantidad']
            offer.precioUnitario = json_offer['precio_unitario']
            offer.total = json_offer['total']
            offer.save()
            return HttpResponse(serializers.serialize("json", [offer]))
        else:
            return JsonResponse({"mensaje": "error"})


@csrf_exempt
def request_offers(request, user_id):
    if request.method == 'GET':
        productor = Productor.objects.filter(usuarioId_id=user_id).first()
        oferta = Oferta.objects.filter(productor_id=productor.pk).all().values('pk', 'producto__nombre', 'cantidad',
                                                                               'total', 'fecha', 'estado')
        productores = json.loads(json.dumps(list(oferta), cls=DateTimeEncoder))
        return JsonResponse(productores, safe=False)


@csrf_exempt
def request_offer(request, pk):
    if request.method == 'GET':
        oferta = Oferta.objects.filter(id=pk).all().values('producto__id', 'cantidad', 'precioUnitario', 'total',
                                                           'pk').first()
        return JsonResponse(oferta, safe=False)


@csrf_exempt
def request_products(request, user_id):
    if request.method == 'GET':
        productor = Productor.objects.filter(usuarioId_id=user_id).first()
        productor_id = productor.pk
        productos = Productor_Producto.objects.filter(
            Q(productor_id=productor_id)).values('producto_id__pk', 'producto_id__nombre')
        productos = json.loads(json.dumps(list(productos)))
        project_productos = []
        for product in productos:
            project_product = {'id': product['producto_id__pk'], 'value': product['producto_id__nombre']}
            project_productos.append(project_product)
        return JsonResponse(project_productos, safe=False)


@csrf_exempt
def product_unit(request, product_id):
    if request.method == 'GET':
        product = Producto.objects.filter(id=product_id).first()
        return JsonResponse(product.unidadMedida.nombre, safe=False)


@csrf_exempt
def producers(request):
    if request.method == 'GET':
        productor = Productor.objects.filter(pk__in=[e.productor.id for e in Oferta.objects.all()])
        return HttpResponse(serializers.serialize("json", productor))


def products(request):
    if request.method == 'GET':
        producto = Producto.objects.filter(pk__in=[e.producto.id for e in Oferta.objects.all()])
        return HttpResponse(serializers.serialize("json", producto))


@csrf_exempt
def index(request):
    return render(request, 'index.html')


@csrf_exempt
def delete_offer(request):
    jsonData = json.loads(request.body)
    if request.method == 'DELETE':
        offer = Oferta.objects.get(pk=jsonData['oferta_pk'])
        if offer is not None:
            offer.delete()
            return JsonResponse({"mensaje": "ok"})
        else:
            return JsonResponse({"mensaje": "error"})


class DateTimeEncoder(json.JSONEncoder):
    def default(self, obj):
        if hasattr(obj, 'isoformat'):
            return obj.isoformat()
        elif isinstance(obj, decimal.Decimal):
            return float(obj)
        elif isinstance(obj, ModelState):
            return None
        else:
            return json.JSONEncoder.default(self, obj)
