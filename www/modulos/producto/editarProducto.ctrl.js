/**
 * Created by IvanGarcia on 17/04/2016.
 */
(function (ng) {
    var mod = ng.module('editarProductoModule');

    mod.controller('editarProductoCtrl', ['$scope', '$routeParams','editarProductoService', '$window', function ($scope,$routeParams,editarProductoService, $window) {
        function responseError(response) {
            console.log(response);
        }
          this.getProduct = function () {
            editarProductoService.getProduct($routeParams.idProject).then(function (response) {
                $scope.projects = response.data[0];
            }, responseError);

        };
            this.editProject = function () {

            return editarProductoService.editProduct($scope.projects).then(function (response) {
                $scope.success = 'OK';
                  if($scope.success === 'OK'){
                    window.location.assign('#/productos');
                    window.location.reload(true);
                }else{
                    $scope.error = true;
                }
            }, responseError);
        };
    }]);


})(window.angular);
