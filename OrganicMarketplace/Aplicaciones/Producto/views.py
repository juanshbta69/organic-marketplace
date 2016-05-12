import os

from django.core.files.base import ContentFile
from django.shortcuts import render
import json
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from OrganicMarketplace.Aplicaciones.Producto.models import Producto
from OrganicMarketplace.Aplicaciones.UnidadMedida.models import UnidadMedida
import time


@csrf_exempt
def productos(request):
    productos = Producto.objects.all()
    return HttpResponse(serializers.serialize("json", productos))

@csrf_exempt
def buscar_productos(request, nombre):
    productos = Producto.objects.filter(nombre__icontains=nombre)
    return HttpResponse(serializers.serialize("json", productos))

@csrf_exempt
def createProduct(request):
    if request.method == 'POST':

        objs = json.loads(request.body)
        unidad = UnidadMedida()
        unidad.nombre =objs['unitName']
        unidad.abreviatura =objs['unitAb']
        unidad.save()

        product = Producto()
       # unidadMedida = UnidadMedida.objects.get(id=objs.get('pk'))
        product.nombre = objs['name']
        product.descripcion = objs['description']
        product.cantidadMinima = objs['minimum']
        product.unidadMedida=unidad

        base64_string = objs['imageFile'].encode('utf-8')
        print objs['imageFile']
        print base64_string

        filename = str(time.time())+".png"

        # decoding base string to image and saving in to your media root folder
        fh = open(os.path.join("photos/", filename), "wb")
        fh.write(bytes(base64_string.decode('base64')))
        fh.close()

        # saving decoded image to database
        decoded_image = base64_string.decode('base64')
        product.imagen = ContentFile(decoded_image, filename)
        product.save()


    return JsonResponse({})

@csrf_exempt
def getProducts(request):
    if request.method == 'GET':
        products = Producto.objects.all()
        return HttpResponse(serializers.serialize("json",products,use_natural_foreign_keys=True, use_natural_primary_keys=True))
    if request.method == 'PUT':
        objs = json.loads(request.body.decode('utf-8'))

        product = Producto.objects.get(id=objs.get('pk'))
        product.nombre = objs['name']
        product.descripcion = objs['description']
        product.cantidadMinima = objs['minimum']
        product.save()
        return HttpResponse(serializers.serialize("json",{product}))

    if request.method == 'DELETE':
            objs = json.loads(request.body.decode('utf-8'))
            product = Producto.objects.get(id=objs.get('pk'))
            product.delete()
            return HttpResponse(serializers.serialize("json",""))

@csrf_exempt
def getSingleProduct(request,idProduct):
    print idProduct
    designs = Producto.objects.filter(id=idProduct)
    return HttpResponse(serializers.serialize("json",designs,use_natural_foreign_keys=True, use_natural_primary_keys=True))
