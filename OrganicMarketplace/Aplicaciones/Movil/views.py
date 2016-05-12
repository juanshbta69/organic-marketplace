# coding=utf-8
import json

import datetime
from copy import deepcopy

from django.contrib.auth import authenticate, login, logout
from django.core.cache import cache
from django.core.paginator import Paginator, EmptyPage
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from OrganicMarketplace.Aplicaciones.Compra.models import Compra, Compra_Producto
from OrganicMarketplace.Aplicaciones.Consumidor.models import Consumidor
from OrganicMarketplace.Aplicaciones.Oferta.models import Oferta
from OrganicMarketplace.Aplicaciones.Producto.models import Producto


@csrf_exempt
def iniciar_sesion(request):
    if request.method == 'POST':
        json_request = json.loads(request.body)
        username = json_request['username']
        password = json_request['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)

            return JsonResponse({
                "username": username,
                "status": "OK",
                "message": "El usuario ha iniciado sesión"
            })
        else:
            return JsonResponse({
                "username": username,
                "status": "ERROR",
                "message": "Usuario o Clave incorrecta"
            })


@csrf_exempt
def cerrar_sesion(request):
    logout(request)

    return JsonResponse({
        "status": "OK",
        "message": "El usuario ha finalizado sesión"
    })


@csrf_exempt
def productos(request):
    respuesta = []
    if request.method == 'GET':
        # respuesta = obtener_productos_semana()
        respuesta = productos_semana

    return JsonResponse(respuesta, safe=False)


@csrf_exempt
def productos_por_pagina(request, page):
    respuesta = []
    if request.method == 'GET':
        # respuesta = obtener_productos_semana()
        respuesta = productos_semana

        try:
            paginador = Paginator(respuesta, 50)
            pagina = paginador.page(page)
            respuesta = pagina.object_list
        except EmptyPage:
            respuesta = []

    return JsonResponse(respuesta, safe=False)


# Instalar memcache (pip install python-memcached)
@csrf_exempt
def agregar_producto_carrito(request):
    respuesta = {}
    if request.method == 'PUT':
        json_request = json.loads(request.body)
        username = json_request['username']
        producto = json_request['id_product']
        cantidad = json_request['quantity']

        if str(username) == str(request.user) and request.user.is_authenticated():
            carrito = cache.get(username)
            if carrito is not None:
                carrito.append({
                    "producto": producto,
                    "cantidad": cantidad
                })
            else:
                carrito = [{
                    "producto": producto,
                    "cantidad": cantidad
                }]

            cache.set(username, carrito)
            print carrito

            respuesta = {
                "status": "OK",
                "message": "Agregado al Carrito."
            }
        else:
            respuesta = {
                "status": "ERROR",
                "message": "El usuario no esta autenticado."
            }

    return JsonResponse(respuesta, safe=False)


@csrf_exempt
def confirmar_compra(request):
    respuesta = {}
    if request.method == 'POST':
        json_request = json.loads(request.body)
        username = json_request['username']
        password = json_request['password']
        confirmacion = json_request['confirmation']
        productos = deepcopy(productos_semana)

        items_compra = []
        total_compra = 0

        if confirmacion:
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)

                carrito = cache.get(username)
                if carrito is not None:
                    for producto in productos:
                        print 'Stock de ' + producto['name'] + ': ' + str(producto['stock'])
                        cantidad = 0
                        for item_carrito in carrito:
                            if str(item_carrito['producto']) == str(producto['id']):
                                cantidad += item_carrito['cantidad']

                        valor = producto['price'] * cantidad
                        print 'Cantidad total de ' + producto['name'] + ": " + str(cantidad) + ', valor: $' + str(valor)

                        total_compra += valor

                        if cantidad <= producto['stock']:
                            if producto['stock'] > 0:
                                producto['stock'] -= cantidad
                                items_compra.append({
                                    "producto": producto['id'],
                                    "cantidad": cantidad,
                                    "valor": valor
                                })
                            else:
                                return JsonResponse({
                                    "status": "ERROR",
                                    "message": "Producto Agotado."
                                })
                        else:
                            return JsonResponse({
                                "status": "ERROR",
                                "message": "No hay suficiente stock."
                            })

                        print 'Nuevo stock de ' + producto['name'] + ': ' + str(producto['stock'])

                    respuesta = registrar_compra(user, productos, items_compra, total_compra)

                else:
                    respuesta = {
                        "status": "ERROR",
                        "message": "Su Carrito esta vacio."
                    }
        else:
            cache.delete(username)

    return JsonResponse(respuesta, safe=False)


@csrf_exempt
def productos_comprados(request):
    respuesta = []
    if request.method == 'GET':
        consumidor = Consumidor.objects.get(usuarioId=request.user.pk)
        ultima_compra = Compra.objects.filter(consumidor=consumidor.pk).order_by("-id")[0]
        detalles_compra = Compra_Producto.objects.filter(compra_id=ultima_compra.pk)
        for detalle_compra in detalles_compra:
            respuesta.append({
                "id": detalle_compra.producto.pk,
                "name": detalle_compra.producto.nombre,
                "quantity": detalle_compra.cantidad,
                "price": detalle_compra.valor,
                "unit": detalle_compra.producto.unidadMedida.abreviatura,
                "total": int(detalle_compra.valor)
            })

    return JsonResponse(respuesta, safe=False)


def registrar_compra(user, productos, items_compra, total_compra):
    print 'Usuario que va a registrar la compra: [' + str(user.pk) + ', ' + user.username + ']'

    try:
        consumidor = Consumidor.objects.get(usuarioId=user.pk)
        compra = Compra()
        compra.consumidor = consumidor
        compra.totalCompra = total_compra
        compra.estado = "Pendiente entrega"
        compra.save()

        for item_compra in items_compra:
            if item_compra['cantidad'] > 0:
                compra_producto = Compra_Producto()
                compra_producto.compra = compra
                producto_comprado = Producto.objects.get(pk=item_compra['producto'])
                compra_producto.producto = producto_comprado
                compra_producto.cantidad = item_compra['cantidad']
                compra_producto.valor = item_compra['valor']
                compra_producto.save()

        global productos_semana
        productos_semana = productos
        cache.delete(user.username)

        respuesta = {
            "status": "OK",
            "message": "Confirmada la compra."
        }
    except Exception as e:
        print "Error: {0}".format(e.message)

        respuesta = {
            "status": "ERROR",
            "message": "Ocurrio un erroral registrar la compra."
        }

    return respuesta


def obtener_productos_semana():
    resultado = []
    productos = Producto.objects.all()

    for producto in productos:
        ofertas = Oferta.objects.filter(producto__pk=producto.pk)
        # print 'Numero de ofertas de ' + producto.nombre + ': ' + str(len(ofertas))
        cantidad = 0
        precio_venta = 0
        for oferta in ofertas:
            if es_oferta_semana(oferta):
                cantidad += oferta.cantidad
                precio_venta += oferta.precioUnitario
        # print 'Cantidad total de ' + producto.nombre + ': ' + str(cantidad_producto) + ' ' +
        # producto.unidadMedida.abreviatura
        if len(ofertas) > 0:
            precio_venta /= len(ofertas)
        # print 'Y el precio de venta es de: ' + str(precio_venta)
        if cantidad > 0:
            resultado.append({
                "id": producto.pk,
                "name": producto.nombre,
                "price": precio_venta,
                "unit": producto.unidadMedida.abreviatura,
                "premium": producto.premium,
                "image": producto.imagen.url,
                "stock": cantidad
            })

    return resultado


def es_oferta_semana(oferta):
    fecha_actual = datetime.datetime.now().date()
    # print '*** Fecha actual: ' + str(fecha_actual)
    fecha = oferta.fecha
    # print '*** Fecha: ' + str(fecha)
    # print '*** Dia fecha: ' + str(fecha.weekday())
    dias = 0 - fecha.weekday()
    # print '*** Dias: ' + str(dias)
    if dias <= 0:
        dias += 7
    # print '*** Nuevos dias: ' + str(dias)
    fecha_inicio = fecha + datetime.timedelta(dias)
    # print '*** Fecha inicio: ' + str(fecha_inicio)
    fecha_fin = fecha_inicio + datetime.timedelta(6)
    # print '*** Fecha fin: ' + str(fecha_fin)
    # print '*** Estado de la oferta: ' + oferta.estado
    if oferta.estado == 'aceptada' and fecha_inicio <= fecha_actual <= fecha_fin:
        oferta_semana = True
    else:
        oferta_semana = False

    # print 'La oferta ' + str(oferta.pk) + ' es de la semana actual: ' + str(oferta_semana)

    return oferta_semana


# Obtención global de los prodcutos de la semana
productos_semana = obtener_productos_semana()
