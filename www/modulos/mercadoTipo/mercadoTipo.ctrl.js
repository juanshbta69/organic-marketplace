(function (ng) {
    var mod = ng.module('mercadoTipoModule');

    mod.controller('mercadoTipoCtrl', ['$scope', "$location", 'mercadoTipoService', '$routeParams', function ($scope, $location, mercadoTipoService, $routeParams) {
        $scope.idSelected = 0;
        $scope.only_numbers = /^[1-9][0-9]{0,2}(?:,?[0-9]{3}){0,3}(?:\.[0-9]{1,2})?$/;
        var responseError = "";
        $scope.creating = false;

        var refreshLists = function(id) {
            mercadoTipoService.requestMarketProducts(id).then(function (response) {
                $scope.typeMarketsProducts = response.data;
            }, responseError);
            mercadoTipoService.requestMarketAvailableProducts(id).then(function (response) {
                $scope.typeMarketsAvailableProducts = response.data;
            }, responseError);
        }

        var refreshMarket = function() {
            return mercadoTipoService.requestMarket().then(function (response) {
                $scope.typeMarkets = response.data;
            }, responseError);
        }

        this.toCreate = function() {
            $scope.creating = true;
        }

        this.toList = function() {
            $scope.creating = false;
        }

        this.requestMarket = function () {
            refreshMarket();
        };

        this.selectTypeMarket = function (id) {
            if ($scope.idSelected == id) {
                $scope.idSelected = 0;
            } else {
                $scope.idSelected = id;
            }
        }

        this.addProduct = function (index, id) {
            cantidad = angular.element(document.querySelector('#cantidad_' + index)).val();
            mercadoTipoService.addProduct(id, cantidad, $scope.idSelected).then(function (response) {
                 refreshLists($scope.idSelected);
            }, responseError);
        }

        this.deleteProduct = function (id) {
            mercadoTipoService.deleteProduct(id).then(function (response) {
                refreshLists($scope.idSelected);
            }, responseError);
        }

        this.saveMarket = function() {
            return mercadoTipoService.saveMarket($scope.new_market).then(function (response) {
                alert('Mercado tipo creado exitosamente ');
                $scope.creating = false;
                refreshMarket();
            }, responseError);
        }

        $scope.$watch('idSelected', function(newValue, oldValue) {
            if (newValue !== 0 && newValue !== oldValue) {
                refreshLists(newValue);
            }
        });

    }]);
})(window.angular);




