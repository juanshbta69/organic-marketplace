/**
 * Created by Juan on 16/04/16.
 */
(function (ng) {
    var mod = ng.module('deliveryDaysAdminModule');

    mod.service('deliveryDaysAdminService', ['$http', 'deliveryDaysAdminContext', function ($http, context) {

        this.getDiasEntrega = function () {
            return $http({
                method: 'GET',
                url: '/diaentrega'
            });
        };

        this.definirDiasEntrega = function (diasEntrega, administradorId) {
            return $http({
                method: 'POST',
                url: '/diaentrega/diasEntrega/',
                data: {
                    diasEntrega: diasEntrega,
                    administradorId: administradorId
                }
            });
        };

    }]);
})(window.angular);