
(function (ng) {
    var mod = ng.module('mercadoTipoModule');

    mod.service('mercadoTipoService', ['$http', 'mercadoTipoContext', function ($http, context) {

        this.requestMarket = function () {
            return $http({
                method: 'GET',
                url: '/mercadotipo/request/'
            });
        };

        this.requestMarketProducts = function (market_id) {
            return $http({
                method: 'GET',
                url: '/mercadotipo/request_products/' + market_id + '/'
            });
        };

        this.requestMarketAvailableProducts = function (market_id) {
            return $http({
                method: 'GET',
                url: '/mercadotipo/request_products_available/' + market_id + '/'
            });
        };

        this.addProduct = function (id, cantidad, mercado_tipo) {
            return $http({
                method: 'POST',
                url: '/mercadotipo/add_product/',
                data: {
                    mercado_tipo: mercado_tipo,
                    producto: id,
                    cantidad: cantidad
                }
            });
        }

        this.deleteProduct = function (id) {
            return $http({
                method: 'DELETE',
                url: '/mercadotipo/delete_product/',
                data: {
                    id: id
                }
            });
        }

        this.saveMarket = function (new_market) {
            return $http({
                method: 'POST',
                url: '/mercadotipo/create/',
                data: {
                    nombre: new_market.nombre,
                    descripcion: new_market.descripcion,
                    imagen: '',
                    precio: new_market.precio
                }
            });
        }

    }]);
})(window.angular);
