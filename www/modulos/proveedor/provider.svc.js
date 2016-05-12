
(function (ng) {
    var mod = ng.module('providerModule');

    mod.service('providerService', ['$http', 'providerContext', function ($http, context) {

        this.logIn = function (username, password) {
            return $http({
                method: 'POST',
                url: context+'/loginProvider/',
                data: {
                    username: username,
                    password: password
                }
            });
        };

        this.requestOffers = function (provider) {
            return $http({
                method: 'GET',
                url: '/oferta/request_offers/' + provider + '/'
            });
        };

        this.requestProducts = function (provider) {
            return $http({
                method: 'GET',
                url: '/oferta/request_products/' + provider + '/'
            });
        };

        this.loadUnit = function (product_id) {
            return $http({
                method: 'GET',
                url: '/oferta/product_unit/' + product_id + '/'
            });
        }

        this.saveOffer = function (new_offer, user_id) {
            return $http({
                method: 'POST',
                url: '/oferta/create_offer/',
                data: {
                    user_id: user_id,
                    producto_pk: new_offer.producto.id,
                    fecha: new Date(),
                    cantidad: new_offer.cantidad,
                    precio_unitario: new_offer.precio,
                    total: new_offer.precio_total
                }
            });
        }

        this.deleteOffer = function (oferta_pk) {
            return $http({
                method: 'DELETE',
                url: '/oferta/delete_offer/',
                data: {
                    oferta_pk: oferta_pk
                }
            });
        }

        this.updateOffer = function (new_offer, offer_id) {
            return $http({
                method: 'POST',
                url: '/oferta/update_offer/',
                data: {
                    id: offer_id,
                    producto_pk: new_offer.producto.id,
                    cantidad: new_offer.cantidad,
                    precio_unitario: new_offer.precio,
                    total: new_offer.precio_total
                }
            });
        }

        this.loadOffer = function (offer_id) {
            return $http({
                method: 'GET',
                url: '/oferta/request_offer/' + offer_id + '/'
            });
        }

    }]);
})(window.angular);
