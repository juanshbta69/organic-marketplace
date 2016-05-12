/**
 * Created by IvanGarcia on 12/03/2016.
 */
(function (ng) {
    var mod = ng.module('crearProductoModule');

    mod.controller('crearProductoCtrl', ['$scope', 'crearProductoService', '$window', function ($scope,crearProductoService, $window) {
        function responseError(response) {
            console.log(response);
        }
  this.createDesign = function () {
            return crearProductoService.createDesign({
                'name':angular.element('#name').val(),
                'description':angular.element('#description').val(),
                'minimum':angular.element('#minimum').val(),
                'imageFile':angular.element('#fileString').val(),
                'unitName':angular.element('#unitName').val(),
                'unitAb':angular.element('#unitAb').val(),

                'pk':6
            }).then(function (response) {
                console.log(response);
                window.alert('Hemos creado exitosamente el producto')
                $scope.message = response.data;
                window.location.assign('#/productores/');
                window.location.reload(true);
            }, responseError);
        };
    }]);


})(window.angular);
