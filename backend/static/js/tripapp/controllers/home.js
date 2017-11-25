'use strict';

var app = angular.module('tripApp.home', ['ngRoute']);

app.controller('HomeCtrl', ['$scope', '$location', function ($scope, $location) {
    $scope.$location = $location;

    $scope.init = function () {
    };
}]);
