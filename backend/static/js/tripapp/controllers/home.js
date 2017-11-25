'use strict';

var app = angular.module('tripApp.home', ['tripApp.service']);

app.controller('HomeCtrl', ['$scope', '$location', 'TripService', function ($scope, $location, TripService) {
    $scope.$location = $location;

    // model
    $scope.term = '';
    $scope.photos = [];
    $scope.result = {};
    $scope.shouldShow = false;
    $scope.hideSearch = false;

    $scope.init = function () {
    };

    $scope.back = function () {
        $scope.shouldShow = true;
        $scope.hideSearch = false;
    }

    $scope.submit = function() {
        if ($scope.term == '') {
            // reset
            $scope.term = '';
            $scope.photos = [];
            $scope.result = {};
            $scope.shouldShow = false;
            $scope.hideSearch = false;
            return;
        }

        TripService
            .searchPhotos($scope.term)
            .then(function (data) {
                $scope.photos = data;
                $scope.shouldShow = true;
            }, function (error) {
                alert(error);
            });
    };

    $scope.getContent = function(photo) {
          var lat = photo.latitude;
          var long = photo.longitude;
          var airport;
          $scope.result.photo = photo.url_c;
          console.log(photo);
          TripService
              .searchForNearestAirport(long,lat)
              .then(function(data) {
                  airport = data[0];
                  console.log(airport);
                  $scope.result.airport = 'Fly to ' + airport.city + ', ' + airport.country ;
                  $scope.result.distance = '(' + Math.round(airport.extras.distance/10)/100 + 'km away from the destination)';
              }, function(error) {
                alert(error);
              })
              .then(function(){
                  console.log(airport.code)
                  TripService.searchFlights(airport.code, '2017-12-05')
                  .then(function(data) {
                    console.log(data);
                    if (data.offers) {
                      $scope.result.offerText = 'Round-trip starting from';
                      $scope.result.offers = '€' + data.offers[0].totalPrice;
                    } else {
                      $scope.result.offerText = 'No flights found';
                      $scope.result.offers = "Get price";
                    }
                  })
              })
              .then(function() {
                TripService.getLocation(lat, long)
                .then(function(data) {
                  console.log(data);
                  $scope.result.location = data.places.place[0].name;
                  $scope.shouldShow = false;
                  $scope.hideSearch = true;
                })
              });


    };
}]);
