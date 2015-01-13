'use strict';

/* Filters */

angular.module('metAppFilters', []).filter('uppercase', function() {
	return function(input) {
		return input.toUpperCase();
	}
});