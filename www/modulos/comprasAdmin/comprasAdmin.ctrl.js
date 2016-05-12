/**
 * Created by Juan on 17/04/16.
 */
(function (ng) {
    var mod = ng.module('purchaseAdminModule');

    mod.controller('purchaseAdminCtrl', ['$scope', 'purchaseAdminService', '$window', '$location', function ($scope, purchaseAdminService, $window, $location) {
        function responseError(response) {
            console.log(response);
        }

        $scope.getPurchases = function () {
            return purchaseAdminService.getPurchases().then(function (response) {
                $scope.purchases = response.data;
                if ($scope.purchases.length == 0) {
                    $("#mensajeInfo").append('<a class="close" data-dismiss="alert" aria-label="close">&times;</a>').append('<strong>No hay pedidos para esta semana!</strong>').show();
                }
            }, responseError);
        };

        $scope.goToPurchaseDetail = function (purchaseId) {
            localStorage.setItem("purchaseId", purchaseId);
            $location.path('/compra_productos');
        };

        $scope.goToPurchases = function () {
            $location.path('/compras');
        };

        $scope.getPurchaseDetail = function () {
            purchaseId = localStorage.getItem("purchaseId");
            return purchaseAdminService.getPurchaseDetail(purchaseId).then(function (response) {
                $scope.totalPurchasePrice = 0;
                $scope.purchaseDetail = response.data;
                for (i = 0; i < $scope.purchaseDetail.length; i++) {
                    $scope.totalPurchasePrice += $scope.purchaseDetail[i].valor;
                }
            }, responseError);
        };

    }]);
})(window.angular);