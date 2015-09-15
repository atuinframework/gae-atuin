'use strict';
var gulp = require('gulp-help')(require('gulp')),
	fs = require('fs'),
	$ = require('gulp-load-plugins')(),
	paths = require('../paths');


gulp.task(	'npm',
			false,
			function() {
				gulp.src('package.json')
				.pipe($.plumber())
				.pipe( $.start() );
			}
);