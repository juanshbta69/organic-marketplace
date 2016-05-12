/**
 * Created by IvanGarcia on 12/03/2016.
 */
(function (ng) {
    var mod = ng.module('registroProveedorModule');

    mod.controller('registroProveedorCtrl', ['$scope', 'registroProveedorService', '$window', function ($scope,registroProveedorService, $window) {
        function responseError(response) {
            console.log(response);
        }

  this.registerManager = function(){
            return registroProveedorService.registerManager({
                'usuario':angular.element('#user').val(),
                'nombre':angular.element('#name').val(),
                'apellido':angular.element('#lastName').val(),
                'descripcion':angular.element('#description').val(),
                'direccion':angular.element('#address').val(),
                'telefono':angular.element('#phone').val(),
                'latitud':angular.element('#latitude').val(),
                'longitud':angular.element('#longitude').val(),
                'extension':angular.element('#extension').val(),
                'password':angular.element('#password').val(),
                'email':angular.element('#email').val()
            }).then(function (response) {
                console.log(response)
                $window.location.href = '#/productores';
                $window.alert('Productor creado exisosamente!')
            }, responseError);
        };

    }]);



})(window.angular);
