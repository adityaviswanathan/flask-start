// module.exports = function($routeProvider, $locationProvider) {
// 	$routeProvider
// 		.when('/', {
// 			templateUrl: 'static/partials/landing.html',
// 			controller: 'IndexController'
// 		})
// 		.when('/about', {
// 			templateUrl: 'static/partials/about.html',
// 			controller: 'AboutController'
// 		})
// 		.when('/users', {
// 			templateUrl: 'static/partials/post-list.html',
// 			controller: 'PostListController'
// 		})
// 		.when('/users/:userId', {
// 			templateUrl: '/static/partials/post-detail.html',
// 			controller: 'PostDetailController'
// 		})
// 		.when('/login', {
// 			templateUrl: '/static/partials/login.html',
// 			controller: 'LoginController'
// 		})
// 		/* Create a "/blog" route that takes the user to the same place as "/post" */
// 		.when('/blog', {
// 			templateUrl: 'static/partials/post-list.html',
// 			controller: 'PostListController'
// 		})
// 		.otherwise({
// 			redirectTo: '/'
// 		});

// 	$locationProvider.html5Mode(true);
// };