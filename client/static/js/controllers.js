'use strict';

/* Controllers */

function IndexController($scope) {
	$scope.hi = 'hello';
}

function AboutController($scope) {
	$scope.hi = 'hello';
}

function UserController($scope) {
	// var users = User.get({}, function(users) {
	// 	$scope.users = users.objects;
	// });

	$scope.hi = "sup";
	console.log("hello");
}

function LoginController($scope, $http) {

	

	// $http.post('signup')
	// 	.success(function(data, status, headers, config) {
	// 		if(data['result'] == 'error') {
	// 			console.log('ERROR');
	// 		} else {
	// 			$console.log(data['user'])
	// 			$location.path('/about')
	// 		}
	// 	})
}

function PostListController($scope, User) {
	var postsQuery = User.get({}, function(users) {
		$scope.users = users.objects;
	});
}

function PostDetailController($scope, $routeParams, User) {
	var postQuery = User.get({ userId: $routeParams.userId }, function(user) {
		$scope.user = user;
	});
}
