/**
 * Created by IvanGarcia on 16/04/2016.
 */
(function (ng) {
    var mod = ng.module('productoModule');

    mod.service('productoService', ['$http', 'productoContext', function ($http, context) {


     this.getOffers = function () {
                return $http({
                    method: 'GET',
                    url: '/producto/productos/'
                });
    };
           this.deleteProduct = function (id) {
                return $http({
                    method: 'DELETE',
                    url: '/producto/productos/',
                    data:{
                        pk:id
                    }
                });
        };
    }]);
})(window.angular);