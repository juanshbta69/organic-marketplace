
(function (ng) {
    var mod = ng.module('categoriaModule');

    mod.service('categoriaService', ['$http', 'categoriaContext', function ($http, context) {


        this.categorias = function () {
            return $http({
                method: 'GET',
                url: '/categoria/'
            });
        };


        this.grabarCategoria = function (nueva_categoria) {
            return $http({
                method: 'POST',
                url: '/categoria/',
                data: {
                    nombre: nueva_categoria.nombre,
                    descripcion: nueva_categoria.descripcion
                }
            });
        }

        this.actualizarCategoria = function (nueva_categoria, categoria_id) {
            return $http({
                method: 'PUT',
                url: '/categoria/',
                data: {
                    pk: categoria_id,
                    nombre: nueva_categoria.nombre,
                    descripcion: nueva_categoria.descripcion
                }
            });
        }

        this.cargarCategoria = function (categoria_id) {
            return $http({
                method: 'GET',
                url: '/categoria/' + categoria_id + '/'
            });
        }

        this.eliminarCategoria = function (categoria_id) {
            return $http({
                method: 'DELETE',
                url: '/categoria/',
                data: {
                    pk: categoria_id
                }
            });
        }

    }]);
})(window.angular);
