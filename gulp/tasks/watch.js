'use strict';
var gulp = require('gulp-help')(require('gulp')),
	$ = require('gulp-load-plugins')(),
	paths = require('../paths');

gulp.task(	'watch',
			false,
			function() {
				gulp.watch(paths.static.src.root + '/css/*', ['css']);
				gulp.watch(paths.static.src.root + '/css/admin/*', ['css_admin']);
				gulp.watch(paths.static.src.root + '/js/*', ['js']);
				gulp.watch(paths.static.src.root + '/js/admin/*', ['js_admin']);
			}
);
