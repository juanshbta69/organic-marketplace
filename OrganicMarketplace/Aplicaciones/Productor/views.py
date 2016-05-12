import json

from django.contrib.auth import authenticate, login
from django.core import serializers
from django.db.models import Q
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from OrganicMarketplace.Aplicaciones.Producto.models import Producto
from OrganicMarketplace.Aplicaciones.Productor.models import Productor_Producto
from .models import Productor
from django.contrib.auth.models import User

@csrf_exempt
def index(request):
    return render(request, 'index.html')

@csrf_exempt
def administracion(request):
    return render(request, 'ingresoAdmin.html')

@csrf_exempt
def proveedor(request):
    return render(request, 'ingresoProveedor.html')

@csrf_exempt
def dashboardAdmin(request):
    return render(request, 'dashboardAdmin.html')

@csrf_exempt
def dashboardProvider(request):
    return render(request, 'dashboardProvider.html')

@csrf_exempt
def createOffer(request):
    return render(request, 'createOffer.html')

@csrf_exempt
def test(request):
    lista_trabajadores = Productor.objects.all()
    return HttpResponse(serializers.serialize("json", lista_trabajadores))


@csrf_exempt
def test2(request):
    return JsonResponse({"mensaje": "Funciona!!"})


@csrf_exempt
def loginAdmin(request):
    if request.method == 'POST':
        jsonUser = json.loads(request.body)
        username = jsonUser['username']
        password = jsonUser['password']
        user = authenticate(username=username, password=password)
        if user is not None and user.is_superuser == True:
            login(request, user)
            return HttpResponse(serializers.serialize("json", [user]))
        else:
            return JsonResponse({"mensaje": "error"})


@csrf_exempt
def loginProvider(request):
    if request.method == 'POST':
        jsonUser = json.loads(request.body)
        username = jsonUser['username']
        password = jsonUser['password']
        user = authenticate(username=username, password=password)
        if user is not None and user.is_superuser == False:
            login(request, user)
            return HttpResponse(serializers.serialize("json", [user]))
        else:
            return JsonResponse({"mensaje": "error"})


@csrf_exempt
def agregar_producto(request, productor_pk, producto_pk):

    if request.method == 'POST':
        productor = Productor.objects.get(pk=productor_pk)
        producto = Producto.objects.get(pk=producto_pk)
        if productor is not None and producto is not None:
            productor_producto = Productor_Producto()
            productor_producto.productor = productor
            productor_producto.producto = producto
            productor_producto.save()
            return HttpResponse(serializers.serialize("json", [productor_producto]))
        else:
            return JsonResponse({"mensaje": "error"})


@csrf_exempt
def eliminar_producto(request, productor_pk, producto_pk):
    if request.method == 'DELETE':
        productor_producto = Productor_Producto.objects.filter(productor=productor_pk, producto=producto_pk)
        if productor_producto is not None:
            productor_producto.delete()
            return JsonResponse({"mensaje": "ok"})
        else:
            return JsonResponse({"mensaje": "errbor"})


@csrf_exempt
def gestionar_producto_productor(request):
    jsonData = json.loads(request.body)
    if request.method == 'POST':
        return agregar_producto(request, jsonData['productor_pk'], jsonData['producto_pk'])
    elif request.method == 'DELETE':
        return eliminar_producto(request, jsonData['productor_pk'], jsonData['producto_pk'])


@csrf_exempt
def buscar_productores(request, nombre):
    productores = Productor.objects.filter(
        Q(usuarioId__first_name__icontains=nombre) | Q(usuarioId__last_name__icontains=nombre)).values('pk','usuarioId__first_name','usuarioId__last_name','telefono')
    if productores:
        productores=json.loads(json.dumps(list(productores)))
        return JsonResponse(productores, safe=False)
    else:
        return JsonResponse({"mensaje": "No hay coincidencias"})

@csrf_exempt
def productores(request):
    productores = Productor.objects.all().values('pk','usuarioId__first_name','usuarioId__last_name','telefono')
    productores=json.loads(json.dumps(list(productores)))
    return JsonResponse(productores, safe=False)

@csrf_exempt
def buscar_productos_productores(request,productor_id , nombre):
    productores = Productor_Producto.objects.filter(
        Q(productor_id=productor_id) & Q(producto_id__nombre__icontains=nombre)).values('pk','producto_id__pk','producto_id__nombre','producto_id__imagen')
    productores=json.loads(json.dumps(list(productores)))
    return JsonResponse(productores, safe=False)

@csrf_exempt
def lista_productos_productores(request,productor_id):
    productores = Productor_Producto.objects.filter(productor_id=productor_id).values('pk','producto_id__pk','producto_id__nombre','producto_id__imagen')
    productores=json.loads(json.dumps(list(productores)))
    return JsonResponse(productores, safe=False)

@csrf_exempt
def lista_productos_productores_faltantes(request,productor_id):
    productores = Producto.objects.raw('SELECT * FROM "Producto_producto" LEFT OUTER JOIN "Productor_productor_producto" ON ("Productor_productor_producto"."producto_id" = "Producto_producto"."id" AND "Productor_productor_producto"."productor_id" = %s) WHERE "Productor_productor_producto"."producto_id" is null', [productor_id])
    return HttpResponse(serializers.serialize("json", productores))

@csrf_exempt
def buscar_productos_productores_faltantes(request,productor_id, nombre):
    productores = Producto.objects.raw('SELECT * FROM "Producto_producto" LEFT OUTER JOIN "Productor_productor_producto" ON ("Productor_productor_producto"."producto_id" = "Producto_producto"."id" AND "Productor_productor_producto"."productor_id" = %s) WHERE "Productor_productor_producto"."producto_id" is null AND lower("Producto_producto"."nombre") like lower(%s)', [productor_id,'%'+nombre+'%'])
    return HttpResponse(serializers.serialize("json", productores))

@csrf_exempt
def registerProducer(request):
    if request.method == 'POST':
        objs = json.loads(request.body)
        message = ''

        usernames = objs['usuario']
        names = objs['nombre']
        lastnames = objs['apellido']
        description = objs['descripcion']
        address = objs['direccion']
        phone = objs['telefono']
        latitude = objs['latitud']
        longitude = objs['longitud']
        ext = objs['extension']
        contrasenia = objs['password']
        email = objs['email']



        userQS = User.objects.filter(username=usernames)
        userList = list(userQS[:1])
        if userList:
            return HttpResponse(status=400)


        userModel = User.objects.create_user(username=usernames, password=contrasenia)
        userModel.first_name=names
        userModel.last_name=lastnames
        userModel.email=email
        userModel.username=usernames
        userModel.save()
        print 'Se crea el usuario'

        manager = Productor()
        manager.descripcion=description
        manager.direccion=address
        manager.telefono=phone
        manager.latitud=latitude
        manager.longitud=longitude
        manager.extension=ext
        manager.usuarioId=userModel
        manager.save()
        print 'Se crea el productor'
        message = 'OK'


        return JsonResponse({'url':message})