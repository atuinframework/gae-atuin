'use strict';
var gulp = require('gulp-help')(require('gulp')),
	$ = require('gulp-load-plugins')(),
	paths = require('../paths');

gulp.task(	'run',
			'Run development server.',
			function() {
				gulp.src('dev.sh')
					.pipe($.start( [{
						match: /dev.sh$/,
						cmd: 'dev_appserver.py app'
					}]));
			}
);

gulp.task(	'monitor',
			'Real time check for css and js.',
			function() {
				$.sequence(['css', 'css_admin'], ['js', 'js_admin'], 'watch')();
			}
);