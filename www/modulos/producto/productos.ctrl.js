/**
 * Created by IvanGarcia on 12/03/2016.
 */
(function (ng) {
    var mod = ng.module('productoModule');

    mod.controller('productoCtrl', ['$scope', 'productoService', '$window', function ($scope,productoService, $window) {
        function responseError(response) {
            console.log(response);
        }
  this.getOffers = function () {
            return productoService.getOffers().then(function (response) {
                $scope.offers = response.data;
            }, responseError);
        };
         this.deleteProduct = function (pk) {
            return productoService.deleteProduct(pk).then(function (response) {
                window.location.reload(true);
            }, responseError);
        };
    }]);


})(window.angular);
