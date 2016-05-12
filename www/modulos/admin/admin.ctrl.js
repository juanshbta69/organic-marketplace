/**
 * Created by JuanDa on 10/03/2016.
 */
(function (ng) {
    var mod = ng.module('adminModule');

    mod.controller('adminCtrl', ['$scope',"$location", 'adminService', function ($scope,$location, adminService) {
        $scope.user={};

        $scope.getProductos = function () {
            return adminService.getProductos($scope.productor.pk,"").then(function (response) {
                $scope.productos=response.data;
            }, responseError);
        };

        $scope.buscarProductos = function () {
            return adminService.getProductos($scope.productor.pk,$("#buscarProducto").val()).then(function (response) {
                $scope.productos=response.data;
            }, responseError);
        };

        $scope.getProductor_Productos = function () {
            return adminService.getProductor_Productos($scope.productor.pk,"").then(function (response) {
                $scope.productor_productos=response.data;
            }, responseError);
        };

        $scope.buscarProductor_Productos = function () {
            return adminService.getProductor_Productos($scope.productor.pk,$("#buscarProductor_Productos").val()).then(function (response) {
                $scope.productor_productos=response.data;
            }, responseError);
        };


        if (localStorage.getItem("adminUser")==undefined && window.location.href.indexOf("dashboard")!=-1){
            window.location='/admin';
        }
        if (localStorage.getItem("adminUser")!=undefined && window.location.href.indexOf("dashboard")!=-1){
            $scope.adminUser=JSON.parse(localStorage.getItem("adminUser"));
             $("#nombreAdmin").text($scope.adminUser.fields.first_name);
        }

        if (localStorage.getItem("productor")!=undefined && window.location.href.indexOf("productos_productor")!=-1){
            $scope.productor=JSON.parse(localStorage.getItem("productor"));
            $scope.getProductos();
            $scope.getProductor_Productos();
        }

        $scope.errorLogin = false;
        function responseError(response) {
            console.log(response);
        }

        $scope.logout = function () {
            $scope.adminUser=undefined;
            localStorage.clear();
            window.location='/admin';
        };

        $scope.logIn = function () {
            return adminService.logIn($scope.user.username,$scope.user.password).then(function (response) {
                //$scope.message = response.data;
                //alert(JSON.stringify(response.data.mensaje, null, 4));
                if(response.data.mensaje != 'error'){
                    localStorage.setItem("adminUser",JSON.stringify(response.data[0]));
                    window.location='/dashboard';
                }else{
                    $scope.adminUser=response.data;
                    $scope.errorLogin = true;
                }
            }, responseError);
        };

        $scope.getProductores = function () {
            return adminService.getProductores("").then(function (response) {
                $scope.productores=response.data;
            }, responseError);
        };

        $scope.buscarProductores = function () {
            return adminService.getProductores($("#buscar").val()).then(function (response) {
                $scope.productores=response.data;
            }, responseError);
        };

        $scope.agregarProductos = function (productor) {
            localStorage.setItem("productor",JSON.stringify(productor));
            $location.path("/productos_productor");

        };


        $scope.agregarProductor_Producto = function (producto_id) {
            return adminService.agregarProductor_Producto($scope.productor.pk,producto_id).then(function (response) {
                if(response.data.mensaje != 'error'){
                    $scope.getProductos();
                    $scope.getProductor_Productos();
                    $("#mensaje").css("color", "green");
                    $("#mensaje").text("¡Se grabo con éxito!")
                }else{
                    $("#mensaje").css("color", "red");
                    $("#mensaje").text("Error al grabar")
                }
            }, responseError);
        };

        $scope.eliminarProductor_Producto = function (producto_id) {
            return adminService.eliminarProductor_Producto($scope.productor.pk,producto_id).then(function (response) {
                if(response.data.mensaje != 'error'){
                    $scope.getProductos();
                    $scope.getProductor_Productos();
                    $("#mensaje").css("color", "green");
                    $("#mensaje").text("¡Se elimino con éxito!")
                }else{
                    $("#mensaje").css("color", "red");
                    $("#mensaje").text("Error al eliminar")
                }
            }, responseError);
        };



    }]);
})(window.angular);
