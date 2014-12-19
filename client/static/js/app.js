'use strict';

var app = angular.module('AngularFlask', ['angularFlaskServices']);

app.config(['$interpolateProvider', function($interpolateProvider) {
  $interpolateProvider.startSymbol('{[');
  $interpolateProvider.endSymbol(']}');
}]);

app.config(['$routeProvider', '$locationProvider', function($routeProvider, $locationProvider) {
	$routeProvider
		.when('/', {
			templateUrl: 'static/partials/landing.html',
			controller: 'IndexController'
		})
		.when('/about', {
			templateUrl: 'static/partials/about.html',
			controller: 'AboutController'
		})
		.when('/users', {
			templateUrl: 'static/partials/post-list.html',
			controller: 'PostListController'
		})
		.when('/users/:userId', {
			templateUrl: '/static/partials/post-detail.html',
			controller: 'PostDetailController'
		})
		/* Create a "/blog" route that takes the user to the same place as "/post" */
		.when('/blog', {
			templateUrl: 'static/partials/post-list.html',
			controller: 'PostListController'
		})
		.when('/user', {
			templateUrl: 'static/partials/user.html',
			controller: 'UserController'
		})
		.otherwise({
			redirectTo: '/'
		});

	$locationProvider.html5Mode(true);
}]);

// app.config(require('routes.js')); //NEED TO INSTALL REQUIRE JS




