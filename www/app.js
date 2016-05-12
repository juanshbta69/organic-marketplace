/**
 * Created by JuanDa on 10/03/2016.
 */
(function (ng) {

    var organicApp = ng.module('organicApp', [
        'ngRoute',
        'adminModule',
        'providerModule',
        'offerAdminModule',
        'categoriaModule',
        'registroProveedorModule',
        'crearProductoModule',
        'productoModule',
        'editarProductoModule',
        'deliveryDaysAdminModule',
        'purchaseAdminModule',
        'registroProveedorModule',
        'mercadoTipoModule'
    ]);

    organicApp.config(['$routeProvider', function ($routeProvider) {
        $routeProvider
            .when('/ofertas', {
                templateUrl: '../www/modulos/ofertasAdmin/ofertasAdmin.html',
                controller: 'offerAdminCtrl',
                controllerAs: 'ctrl'
            })
            .when('/principal', {
                templateUrl: '../www/modulos/admin/principal.tpl.html',
                controller: 'adminCtrl',
                controllerAs: 'ctrl'
            })
            .when('/loginAdmin', {
                templateUrl: 'LoginAdmin.tpl.html',
                controller: 'adminCtrl',
                controllerAs: 'ctrl'
            })
            .when('/productores', {
                templateUrl: '../www/modulos/admin/gestionProductor.tpl.html',
                controller: 'adminCtrl',
                controllerAs: 'ctrl'
            })
            .when('/productos_productor', {
                templateUrl: '../www/modulos/admin/productosProductor.tpl.html',
                controller: 'adminCtrl',
                controllerAs: 'ctrl'
            })
            .when('/diasEntrega', {
                templateUrl: '../www/modulos/diasEntregaAdmin/diasEntregaAdmin.tpl.html',
                controller: 'deliveryDaysAdminCtrl',
                controllerAs: 'ctrl'
            })
            .when('/compras', {
                templateUrl: '../www/modulos/comprasAdmin/comprasAdmin.tpl.html',
                controller: 'purchaseAdminCtrl',
                controllerAs: 'ctrl'
            })
            .when('/compra_productos', {
                templateUrl: '../www/modulos/comprasAdmin/detallesCompraAdmin.tpl.html',
                controller: 'purchaseAdminCtrl',
                controllerAs: 'ctrl'
            })
              .when('/registro', {
                templateUrl: '../www/modulos/registroProveedor/registroProveedor.html',
                controller: 'registroProveedorCtrl',
                controllerAs: 'ctrl'
            })
            .when('/categorias', {
                templateUrl: '../www/modulos/categorias/categorias.tpl.html',
                controller: 'categoriaCtrl',
                controllerAs: 'ctrl'
            })
            .when('/editar_categoria/:categoria_id', {
                templateUrl: '../www/modulos/categorias/editarCategoria.tpl.html',
                controller: 'categoriaCtrl',
                controllerAs: 'ctrl'
            })
            .when('/crear_categoria', {
                templateUrl: '../www/modulos/categorias/crearCategoria.tpl.html',
                controller: 'categoriaCtrl',
                controllerAs: 'ctrl'
            })
             .when('/crearProducto', {
                templateUrl: '../www/modulos/producto/crearProducto.html',
                controller: 'crearProductoCtrl',
                controllerAs: 'ctrl'
            })
             .when('/productos', {
                templateUrl: '../www/modulos/producto/productos.html',
                controller: 'productoCtrl',
                controllerAs: 'ctrl'
            })
            .when('/edit/:idProject', {
                templateUrl: '../www/modulos/producto/editarProducto.html',
                controller: 'editarProductoCtrl',
                controllerAs: 'ctrl'
            })
            .when('/mercado_tipo', {
                templateUrl: '../www/modulos/mercadoTipo/mercadoTipo.tpl.html',
                controller: 'mercadoTipoCtrl',
                controllerAs: 'ctrl'
            })
            .otherwise('/principal');

    }]);
})(window.angular);
