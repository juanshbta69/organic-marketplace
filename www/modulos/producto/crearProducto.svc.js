/**
 * Created by IvanGarcia on 16/04/2016.
 */
(function (ng) {
    var mod = ng.module('crearProductoModule');

    mod.service('crearProductoService', ['$http', 'crearProductoContext', function ($http, context) {

          this.createDesign = function (data) {
            return $http({
                method: 'POST',
                //url: 'https://ancient-plains-90032.herokuapp.com/login',
                url: '/producto/crear/',
                data: data
            });
        };

    }]);
})(window.angular);