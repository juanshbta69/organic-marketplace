/**
 * Created by IvanGarcia on 17/04/2016.
 */
(function (ng) {
    var mod = ng.module('editarProductoModule');

    mod.service('editarProductoService', ['$http', 'editarProductoContext', function ($http, context) {

  this.getProduct = function (idProject) {
            return $http({
                method: 'GET',
                url: '/producto/cargar/'+idProject
            });
        }
           this.editProduct = function (project) {
            return $http({
                method: 'PUT',
                url: '/producto/productos/',
                data:{
                    name: project.fields.nombre,
                    description: project.fields.descripcion,
                    minimum: project.fields.cantidadMinima,
                    pk: project.pk,
                }
            });
        };

    }]);
})(window.angular);