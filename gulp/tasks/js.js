'use strict';
var gulp = require('gulp-help')(require('gulp')),
	$ = require('gulp-load-plugins')(),
	config = require('../config.js'),
	paths = require('../paths.js'),
	util = require('../util.js');

// public
gulp.task(	'js',
		    false,
			function() {
				return gulp.src(config.src.js)
						.pipe( $.plumber({
							errorHandler: util.onError
						}))
						.pipe($.concat('all.js'))
						.pipe($.size({ title: 'LOG js ' }))
						.pipe($.util.env.type === 'production' ? $.uglify({mangle:true}) : $.util.noop())
						.pipe($.size({ title: 'LOG js:min ' }))
						.pipe(gulp.dest(config.min.js));
			}	
);

// admin specific
gulp.task(	'js_admin',
		    false,
			function() {
				return gulp.src(config.src.js_admin)
						.pipe( $.plumber({
							errorHandler: util.onError
						}))
						.pipe($.concat('all.js'))
						.pipe($.size({ title: 'LOG js_admin ' }))
						.pipe($.util.env.type === 'production' ? $.uglify({mangle:true}) : $.util.noop())
						.pipe($.size({ title: 'LOG js_admin:min ' }))
						.pipe(gulp.dest(config.min.js_admin));
			}	
);
