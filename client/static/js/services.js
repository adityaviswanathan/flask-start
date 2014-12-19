'use strict';

angular.module('angularFlaskServices', ['ngResource'])
	.factory('User', function($resource) {
		return $resource('/api/users/:userId', {}, {
			query: {
				method: 'GET',
				params: { userId: '' },
				isArray: true
			}
		});
	})
	.factory('Login', function($resource) {
		// return $resource('/api/auth', {}, {
		// 	query: {
		// 		method: 'GET', 
		// 		params: {}
		// 	}
		// })
	})
;



