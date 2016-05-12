(function (ng) {
    var mod = ng.module('categoriaModule');

    mod.controller('categoriaCtrl', ['$scope', "$location", 'categoriaService', '$routeParams', function ($scope, $location, categoriaService, $routeParams) {
        $scope.nueva_categoria = {};
        if (localStorage.getItem("adminUser")==undefined && window.location.href.indexOf("dashboard")!=-1){
            window.location='/admin';
        }
        var responseError = "";
        $scope.mostrarCategorias = function () {
            return categoriaService.categorias().then(function (response) {
                $scope.categorias = response.data;
            }, responseError);
        };

        this.grabarCategoria = function () {
            return categoriaService.grabarCategoria($scope.nueva_categoria).then(function (response) {
                $location.path("/categorias");
            }, responseError);
        };


        this.cargarCategoria = function () {
            categoriaService.cargarCategoria($routeParams.categoria_id).then(function (response) {
                $scope.nueva_categoria.nombre = response.data[0].fields.nombre;
                $scope.nueva_categoria.descripcion = response.data[0].fields.descripcion;
            }, responseError);
        };

        this.actualizarCategoria = function () {
            return categoriaService.actualizarCategoria($scope.nueva_categoria, $routeParams.categoria_id).then(function (response) {
                $location.path("/categorias");
            }, responseError);
        };

        this.eliminarCategoria = function (categoria_id) {
            return categoriaService.eliminarCategoria(categoria_id).then(function (response) {
                if (response.data.mensaje=="ok"){
                    $scope.mostrarCategorias();
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




