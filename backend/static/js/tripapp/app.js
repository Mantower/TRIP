'use strict';

var app = angular.module('tripApp', ['ngRoute', 'tripApp.home']);

app.config(['$routeProvider', '$locationProvider', function ($routeProvider, $locationProvider) {
    //$locationProvider.html5Mode(true);
    $locationProvider.hashPrefix('');

    $routeProvider
        .when('/', {
            templateUrl: '/js/tripapp/views/home.html',
            controller: 'HomeCtrl'
        })
        .when('/404', {
            templateUrl: '/js/tripapp/views/404.html'
        })
        .otherwise({
            redirectTo: '/404'
        })
    ;
}]);
