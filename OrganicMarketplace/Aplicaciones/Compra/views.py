import json

#from bson import json_util
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import Compra, Compra_Producto


# Create your views here.
@csrf_exempt
def compras(request):
    if request.method == 'GET':
        compras = Compra.objects.all().values('pk', 'fecha', 'totalCompra', 'estado')

        for compra in compras:
            compra['fecha'] = str(compra['fecha'])

        compras = json.loads(json.dumps(list(compras)))
        return JsonResponse(compras, safe=False)


@csrf_exempt
def detalle_compra(request, pk):
    if request.method == 'GET':
        compra = Compra.objects.get(pk=pk)
        compra_productos = Compra_Producto.objects.filter(compra_id=compra.pk).values('producto_id__nombre',
                                                                                      'mercadoTipo_id__nombre',
                                                                                      'cantidad',
                                                                                      'producto_id__unidadMedida_id__abreviatura',
                                                                                      'valor')
        compra_productos = json.loads(json.dumps(list(compra_productos)))
        return JsonResponse(compra_productos, safe=False)
