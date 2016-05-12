/**
 * Created by IvanGarcia on 12/03/2016.
 */
(function (ng) {
    var mod = ng.module('offerAdminModule');

    mod.service('offerAdminService', ['$http', 'offerAdminContext', function ($http, context) {

        this.getOffers = function () {
                return $http({
                    method: 'GET',
                    url: '/oferta/ofertas'
                });
    };
          this.getProducer = function () {
                return $http({
                    method: 'GET',
                    url: '/oferta/producers'
                });
    };
        this.getProducts = function () {
                return $http({
                    method: 'GET',
                    url: '/oferta/productos'
                });
    };
        this.acceptOffer = function (offer) {
            return $http({
                method: 'PUT',
                url: '/oferta/ofertas/',
                data:{
                    estado: "aceptada",
                    id: offer.id
                }
            });
        };
           this.cancelOffer = function (offer) {
            return $http({
                method: 'PUT',
                url: '/oferta/ofertas/',
                data:{
                    estado: "cancelada",
                    id: offer.id
                }
            });
        };
    }]);
})(window.angular);