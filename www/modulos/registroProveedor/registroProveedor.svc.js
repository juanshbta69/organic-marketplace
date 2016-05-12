/**
 * Created by IvanGarcia on 10/04/2016.
 */
(function (ng) {
    var mod = ng.module('registroProveedorModule');

    mod.service('registroProveedorService', ['$http', 'registroProveedorContext', function ($http, context) {

          this.registerManager = function (data) {
            return $http({
                method: 'POST',
                //url: 'https://ancient-plains-90032.herokuapp.com/independents',
                url: '/productor/registro/',
                data:data
            });
        };
    }]);
})(window.angular);