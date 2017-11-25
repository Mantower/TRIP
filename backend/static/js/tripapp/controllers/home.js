'use strict';

var app = angular.module('tripApp.home', ['tripApp.service']);

app.controller('HomeCtrl', ['$scope', '$location', 'TripService', function ($scope, $location, TripService) {
    $scope.$location = $location;

    // model
    $scope.term = '';
    $scope.photos = [];

    $scope.init = function () {
    };

    $scope.submit = function() {
        TripService
            .searchPhotos($scope.term)
            .then(function (data) {
                $scope.photos = data;
            }, function (error) {
                alert(error);
            });
    };
}]);
