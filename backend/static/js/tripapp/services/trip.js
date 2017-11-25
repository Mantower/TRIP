'use strict';

var app = angular.module('tripApp.service', []);

app.factory('TripService', ['$http', '$q', function ($http, $q) {
    return {
        searchPhotos: function (term) {
            var deferred = $q.defer();

            $http
                .get('/v1/search', {
                    'params': {
                        'term': term
                    },
                    timeout: 10000 // 10s
                })
                .then(function (response) {
                    deferred.resolve(response.data);
                }, function (response) {
                    deferred.reject(response.data);
                });

            return deferred.promise;
        },

        getLocation: function (lat, long) {
          var deferred = $q.defer();
          console.log(lat);
          console.log(long);
          $http
              .get('/v1/location', {
                  'params': {
                      'longitude': long,
                      'latitude': lat
                  },
                  timeout: 10000 // 10s
              })
              .then(function (response) {
                  deferred.resolve(response.data);
              }, function (response) {
                  deferred.reject(response.data);
              });

          return deferred.promise;
      },

        searchFlights: function (destinationCode, departureDate) {
            var deferred = $q.defer();

            $http
                .get('/v1/flights', {
                    'params': {
                        'destination_code': destinationCode,
                        'departure_date': departureDate
                    },
                    timeout: 10000 // 10s
                })
                .then(function (response) {
                    deferred.resolve(response.data);
                }, function (response) {
                    deferred.reject(response.data);
                });

            return deferred.promise;
        },

        searchForNearestAirport: function (longitude, latitude) {
            var deferred = $q.defer();

            $http
                .get('/v1/destination', {
                    'params': {
                        'longitude': longitude,
                        'latitude': latitude
                    },
                    timeout: 10000 // 10s
                })
                .then(function (response) {
                    deferred.resolve(response.data);
                }, function (response) {
                    deferred.reject(response.data);
                });

            return deferred.promise;
        },

        randomPhotos: function () {
            var deferred = $q.defer();

            $http
                .get('/v1/random', {
                    timeout: 10000 // 10s
                })
                .then(function (response) {
                    deferred.resolve(response.data);
                }, function (response) {
                    deferred.reject(response.data);
                });

            return deferred.promise;
        }
    };
}]);
