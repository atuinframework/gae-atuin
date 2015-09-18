'use strict';
var gulp = require('gulp-help')(require('gulp')),
	fs = require('fs'),
	$ = require('gulp-load-plugins')(),
	config = require('../config'),
	del = require('del');


gulp.task(	'update:pipinstall',
			false,
			function() {
				return gulp.src('requirements.txt')
						.pipe($.start( [{
							match: /requirements.txt$/,
							cmd: 'pip install -U -r requirements.txt -t ' + config.lib
						}]));
			}
);

gulp.task(	'update:pipcleandist',
			false,
			function() {
				return del(config.lib + '/*.dist-info');
			}
);

gulp.task(	'update:pip',
			false,
			function() {
				return $.sequence('update:pipinstall', 'update:pipcleandist')();
			}
);

gulp.task(	'npm',
			false,
			function() {
				return gulp.src('package.json')
						.pipe($.plumber())
						.pipe( $.start() );
			}
);
