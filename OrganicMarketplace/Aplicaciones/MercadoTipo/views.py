import json

from django.core import serializers
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt

from OrganicMarketplace.Aplicaciones.MercadoTipo.models import MercadoTipo, MercadoTipo_Producto
from OrganicMarketplace.Aplicaciones.Producto.models import Producto


@csrf_exempt
def request(request_market):
    if request_market.method == 'GET':
        market = MercadoTipo.objects.all().values("id", "nombre", "descripcion", "imagen", "precio")
        data = json.loads(json.dumps(list(market)))
        return JsonResponse(data, safe=False)


@csrf_exempt
def request_products(request_market, market_id):
    if request_market.method == 'GET':
        market_product = MercadoTipo_Producto.objects.filter(mercadoTipo_id=market_id).all().values("id", "producto__id", "producto__nombre", "cantidad")
        data = json.loads(json.dumps(list(market_product)))
        return JsonResponse(data, safe=False)


@csrf_exempt
def request_products_available(request_market, market_id):
    if request_market.method == 'GET':
        market_products = MercadoTipo_Producto.objects.filter(mercadoTipo_id=market_id).all().values_list('producto__id', flat=True)
        products = Producto.objects.exclude(id__in=market_products).all().values("id", "nombre")
        data = json.loads(json.dumps(list(products)))
        return JsonResponse(data, safe=False)


@csrf_exempt
def create(request_market):
    json_market = json.loads(request_market.body)
    estado = "activo"
    if request_market.method == 'POST':
        market = MercadoTipo()
        market.nombre = json_market['nombre']
        market.descripcion = json_market['descripcion']
        market.imagen = json_market['imagen']
        market.precio = json_market['precio']
        market.estado = estado
        market.save()
        return HttpResponse(serializers.serialize("json", [market]))


@csrf_exempt
def add_product(request_pm):
    json_pm = json.loads(request_pm.body)
    if request_pm.method == 'POST':
        market = MercadoTipo.objects.get(pk=json_pm['mercado_tipo'])
        product = Producto.objects.get(pk=json_pm['producto'])
        if market is not None and product is not None:
            market_product = MercadoTipo_Producto()
            market_product.mercadoTipo = market
            market_product.producto = product
            market_product.cantidad = json_pm['cantidad']
            market_product.save()
            return HttpResponse(serializers.serialize("json", [market_product]))
        else:
            return JsonResponse({"mensaje": "error"})


@csrf_exempt
def delete_product(request_pm):
    json_pm = json.loads(request_pm.body)
    if request_pm.method == 'DELETE':
        market_product = MercadoTipo_Producto.objects.get(pk=json_pm['id'])
        if market_product is not None:
            market_product.delete()
            return JsonResponse({"mensaje": "ok"})
        else:
            return JsonResponse({"mensaje": "error"})