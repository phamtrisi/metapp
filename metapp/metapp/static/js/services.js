'use strict';

angular.module('metAppServices', ['ngResource'])
	.factory('Post', function($resource) {
		return $resource('/api/post/:postId', {}, {
			query: {
				method: 'GET',
				params: { postId: '' },
				isArray: true
			}
		});
	})
;



