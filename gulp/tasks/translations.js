'use strict';
var gulp = require('gulp-help')(require('gulp')),
	fs = require('fs'),
	$ = require('gulp-load-plugins')(),
	config = require('../config'),
	del = require('del');




gulp.task(	'translations:init',
			false,
			function() {
				if (!$.util.env.lang) {
					$.util.log($.util.colors.red('No --lang specified.') + ' Use like --lang en');
					return;
				}
				return gulp.src('babel.cfg')
						.pipe($.start( [{
							match: /babel.cfg$/,
							cmd: 'pybabel init -i app/messages.pot -d app/translations -l ' + $.util.env.lang
						}]));
			}
);


gulp.task(	'translations:extract',
			false,
			function() {
				return gulp.src('babel.cfg')
						.pipe($.start( [{
							match: /babel.cfg$/,
							cmd: 'pybabel extract -k lazy_gettext -F babel.cfg -o app/messages.pot app'
						}]));
			}
);


gulp.task(	'translations:update',
			false,
			function() {
				return gulp.src('babel.cfg')
						.pipe($.start( [{
							match: /babel.cfg$/,
							cmd: 'pybabel update -i app/messages.pot -d app/translations'
						}]));
			}
);

gulp.task(	'translations:compile',
			false,
			function() {
				return gulp.src('babel.cfg')
						.pipe($.start( [{
							match: /babel.cfg$/,
							cmd: 'pybabel compile -d app/translations'
						}]));
			}
);
