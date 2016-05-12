/**
 * Created by Juan on 17/04/16.
 */
(function (ng) {
    var mod = ng.module('purchaseAdminModule');

    mod.service('purchaseAdminService', ['$http', 'purchaseAdminContext', function ($http, context) {

        this.getPurchases = function () {
            return $http({
                method: 'GET',
                url: '/compra/compras'
            });
        };

        this.getPurchaseDetail = function (purchaseId) {
            return $http({
                method: 'GET',
                url: '/compra/' + purchaseId + '/compra_productos'
            })
        }

    }]);
})(window.angular);