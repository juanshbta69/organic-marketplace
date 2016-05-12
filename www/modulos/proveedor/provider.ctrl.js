(function (ng) {
    var mod = ng.module('providerModule');

    mod.controller('providerCtrl', ['$scope', "$location", 'providerService', '$routeParams', function ($scope, $location, providerService, $routeParams) {
        $scope.userProvider = {};
        $scope.userForm = {};
        $scope.productSelected = "";
        var responseError = "";
        if (localStorage.getItem("providerUser")==undefined && window.location.href.indexOf("ofertas")!=-1){
            window.location='/proveedor';
        }
        if (localStorage.getItem("providerUser")!=undefined && window.location.href.indexOf("ofertas")!=-1){
            $scope.providerUser=JSON.parse(localStorage.getItem("providerUser"));
        }
        this.logIn = function () {
            if ($scope.userForm.username == undefined || $scope.userForm.password == undefined) {
                var error = '{"mensaje": "error"}';
                $scope.errorLogin = true;
                return error;
            }
            return providerService.logIn($scope.userForm.username, $scope.userForm.password).then(function (response) {
                if (response.data.mensaje != 'error') {
                    localStorage.setItem("providerUser", JSON.stringify(response.data[0]));
                    window.location = '/dashboardProvider';
                } else {
                    $scope.userProvider = response.data;
                    $scope.errorLogin = true;
                }
            }, responseError);
        };

        this.logOut = function () {
            $scope.userProvider = undefined;
            localStorage.clear();
            window.location = '/proveedor';
        };

        $scope.requestOffers = function () {
            $scope.userProvider = JSON.parse(localStorage.getItem("providerUser"));
            return providerService.requestOffers($scope.userProvider.pk).then(function (response) {
                $scope.offers = response.data;
            }, responseError);
        };

        $scope.products = {};
        this.requestProducts = function () {
            $scope.userProvider = JSON.parse(localStorage.getItem("providerUser"));
            return providerService.requestProducts($scope.userProvider.pk).then(function (response) {
                $scope.products = response.data;
            }, responseError);
        };

        this.loadUnit = function () {
            if ($scope.productSelected != undefined) {
                providerService.loadUnit($scope.new_offer.producto.id).then(function (response) {
                    $scope.unidad = response.data;
                }, responseError);
            }
        };

        this.deleteOffer = function (offer_pk) {
            return providerService.deleteOffer(offer_pk).then(function (response) {
                if (response.data.mensaje=="ok"){
                    $scope.requestOffers();
                    $("#mensaje").css("color", "green");
                    $("#mensaje").text("¡Se elimino con éxito!")
                }else{
                    $("#mensaje").css("color", "red");
                    $("#mensaje").text("Error al eliminar")

                }

            }, responseError);
        };

        this.saveOffer = function () {
            return providerService.saveOffer($scope.new_offer, $scope.userProvider.pk).then(function (response) {
                alert('Oferta creada exitosamente ');
                $location.path("/ofertas");
            }, responseError);
        };

        this.createOffer = function () {
            $location.path("/createOffer");
        };

        this.updatePrice = function () {
            if ($scope.new_offer.precio != undefined && $scope.new_offer.cantidad != undefined) {
                $scope.new_offer.precio_total = $scope.new_offer.precio * $scope.new_offer.cantidad;
            } else {
                $scope.new_offer.precio_total = 0;
            }
        };

        this.cancel = function () {
            $location.path("/ofertas");
        };

        $scope.new_offer = {};
        this.loadOffer = function () {
            providerService.loadOffer($routeParams.ofertaId).then(function (response) {
                $scope.new_offer.producto = {id: response.data.producto__id};
                $scope.new_offer.cantidad = response.data.cantidad;
                $scope.new_offer.precio = response.data.precioUnitario;
                $scope.new_offer.precio_total = response.data.total;
            }, responseError);
        };

        this.updateOffer = function () {
            return providerService.updateOffer($scope.new_offer, $routeParams.ofertaId).then(function (response) {
                alert('Oferta editada exitosamente');
                $location.path("/ofertas");
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




