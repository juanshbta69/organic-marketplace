/**
 * Created by IvanGarcia on 12/03/2016.
 */
(function (ng) {
    var mod = ng.module('offerAdminModule');

    mod.controller('offerAdminCtrl', ['$scope', 'offerAdminService', '$window', function ($scope,offerAdminService, $window) {
        function responseError(response) {
            console.log(response);
        }


        this.getOffers = function () {
            return offerAdminService.getOffers().then(function (response) {
                $scope.offers = response.data;
            }, responseError);
        };
          this.getProducer = function () {
            return offerAdminService.getProducer().then(function (response) {
                $scope.producer = response.data;
                console.log(response)
            }, responseError);
        };
         this.getProducts = function () {
            return offerAdminService.getProducts().then(function (response) {
                $scope.products = response.data;
            }, responseError);
        };
            this.acceptOffer = function (offer) {
            return offerAdminService.acceptOffer(offer).then(function (response) {
                $scope.success = 'OK';
                  if($scope.success === 'OK'){
                  //  window.location.assign('#/project');
                    window.location.reload();
                }else{
                    $scope.error = true;
                }
            }, responseError);
        };
             this.cancelOffer = function (offer) {
            return offerAdminService.cancelOffer(offer).then(function (response) {
                $scope.success = 'OK';
                  if($scope.success === 'OK'){
                  //  window.location.assign('#/project');
                    window.location.reload();
                }else{
                    $scope.error = true;
                }
            }, responseError);
        };

        $scope.disponibleVenta = function (fecha) {
            var fecha1 = new Date(fecha);
            var dias =8-fecha1.getDay();
            fecha1.setDate(fecha1.getDate() + dias);

            var fecha2 = new Date(fecha1);
            fecha2.setDate(fecha2.getDate() + 6);
            var rango=fecha1.getFullYear()+"-"+(("0" + (fecha1.getMonth()+1)).slice (-2))+"-"+(("0" + fecha1.getDate()).slice (-2))+ " hasta "+fecha2.getFullYear()+"-"+(("0" + (fecha2.getMonth()+1)).slice (-2))+"-"+(("0" + fecha2.getDate()).slice (-2))
            return rango;
        };

    }]);



})(window.angular);
