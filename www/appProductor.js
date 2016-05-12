/**
 * Created by JuanDa on 10/03/2016.
 */
(function (ng) {

    var organicApp = ng.module('organicApp', [
        'ngRoute',
        'adminModule',
        'providerModule',
        'offerAdminModule'
    ]);

    organicApp.config(['$routeProvider', function ($routeProvider) {
        $routeProvider
            .when('/ofertas', {
                templateUrl: '../www/modulos/proveedor/ofertas.tpl.html',
                controller: 'providerCtrl',
                controllerAs: 'ctrl'
            })
            .when('/loginAdmin', {
                templateUrl: 'LoginAdmin.tpl.html',
                controller: 'adminCtrl',
                controllerAs: 'ctrl'
            })
            .when('/crear_oferta', {
                templateUrl: '../www/modulos/proveedor/crearOferta.tpl.html',
                controller: 'providerCtrl',
                controllerAs: 'ctrl'
            })
            .when('/editar_oferta/:ofertaId', {
                templateUrl: '../www/modulos/proveedor/editarOferta.tpl.html',
                controller: 'providerCtrl',
                controllerAs: 'ctrl'
            })
            .when('/productos_productor', {
                templateUrl: '../www/modulos/admin/productosProductor.tpl.html',
                controller: 'adminCtrl',
                controllerAs: 'ctrl'
            })
            .otherwise('/ofertas');

    }]);
})(window.angular);
