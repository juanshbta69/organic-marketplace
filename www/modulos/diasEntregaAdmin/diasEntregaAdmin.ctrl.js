/**
 * Created by Juan on 16/04/16.
 */
(function (ng) {
    var mod = ng.module('deliveryDaysAdminModule');

    mod.controller('deliveryDaysAdminCtrl', ['$scope', 'deliveryDaysAdminService', '$window', function ($scope, deliveryDaysAdminService, $window) {
        function responseError(response) {
            console.log(response);
        }

        if (localStorage.getItem("adminUser")) {
            $scope.usuario = JSON.parse(localStorage.getItem("adminUser"));
        }

        $scope.diasEntrega = {
            semana: [
                {numDia: 1, diaSemana: 'Lunes'},
                {numDia: 2, diaSemana: 'Martes'},
                {numDia: 3, diaSemana: 'Miercoles'},
                {numDia: 4, diaSemana: 'Jueves'},
                {numDia: 5, diaSemana: 'Viernes'},
                {numDia: 6, diaSemana: 'Sabado'},
                {numDia: 7, diaSemana: 'Domingo'}
            ],
            diasSeleccionados: []
        };

        $scope.getDiasEntrega = function () {
            return deliveryDaysAdminService.getDiasEntrega().then(function (response) {
                $scope.diasEntregaActuales = response.data;
            }, responseError);
        };

        $scope.actualizarDiasEntrega = function () {
            if ($scope.diasEntrega.diasSeleccionados.length > 0) {
                return deliveryDaysAdminService.definirDiasEntrega($scope.diasEntrega.diasSeleccionados, $scope.usuario.pk).then(function (response) {
                    if (response.data.mensaje == "ok") {
                        window.location.reload();
                        $("#mensajeExito").append('<a class="close" data-dismiss="alert" aria-label="close">&times;</a>');
                        $("#mensajeExito").append('<strong>Día de entrega actualizados exitosamente!</strong>');
                        $("#mensajeExito").show();
                    } else {
                        $("#mensajeError").append('<a class="close" data-dismiss="alert" aria-label="close">&times;</a>');
                        $("#mensajeError").append('<strong>Ocurrio un error actualizando los datos!</strong>')
                        $("#mensajeError").show();
                    }
                }, responseError);
            } else {
                $("#mensajeAdvertencia").append('<a class="close" data-dismiss="alert" aria-label="close">&times;</a>');
                $("#mensajeAdvertencia").append('<strong>No se han seleccionado días para actualizar!</strong>');
                $("#mensajeAdvertencia").show();
            }
        };
    }]);
})(window.angular);