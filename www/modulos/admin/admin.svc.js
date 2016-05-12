/**
 * Created by JuanDa on 10/03/2016.
 */
(function (ng) {
    var mod = ng.module('adminModule');

    mod.service('adminService', ['$http', 'adminContext', function ($http, context) {

        this.logIn = function (username,password) {
            return $http({
                method: 'POST',
                url: context+'/loginAdmin/',
                data: {
                    username: username,
                    password: password
                }
            });
        };

        this.getProductores = function (buscar) {
            return $http({
                method: 'GET',
                url: '/productor/'+buscar
            });
        };

        this.getProductos = function (producto_id,nombre_producto) {
            if (nombre_producto!=""){
                nombre_producto="/"+nombre_producto;
            }
            return $http({
                method: 'GET',
                url: '/productor/productor_producto_faltantes/'+producto_id+nombre_producto
            });
        };
        this.getProductor_Productos = function (producto_id,nombre_producto) {
            if (nombre_producto!=""){
                nombre_producto="/"+nombre_producto;
            }
            return $http({
                method: 'GET',
                url: '/productor/productor_producto/'+producto_id+nombre_producto
            });
        };
        this.agregarProductor_Producto = function (productor_id,producto_id) {
            return $http({
                method: 'POST',
                url: '/productor/gestion_productor_producto/',
                data: {
                    productor_pk: productor_id,
                    producto_pk: producto_id
                }
            });
        };

        this.eliminarProductor_Producto = function (productor_id,producto_id) {
            return $http({
                method: 'DELETE',
                url: '/productor/gestion_productor_producto/',
                data: {
                    productor_pk: productor_id,
                    producto_pk: producto_id
                }
            });
        };

    }]);
})(window.angular);
