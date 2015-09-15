'use strict';
var gulp = require('gulp-help')(require('gulp')),
	$ = require('gulp-load-plugins')(),
	config = require('../config.js'),
	paths = require('../paths.js'),
	util = require('../util.js');

// public
gulp.task(	'css',
			false,
			function() {
				gulp.src(config.css)
				.pipe($.plumber({
					errorHandler: util.onError
				}))
				.pipe($.sass().on('error', util.onError))
				.pipe($.autoprefixer({
					cascade: false
				}))
				.pipe($.size({ title: 'LOG css' }))
				.pipe( $.util.env.type === 'production' ? $.minifyCss() : $.util.noop())
				.pipe($.size({ title: 'LOG css:min' }))
				.pipe(gulp.dest(paths.static.min.root + "/css"));
			}
);

// admin specific
gulp.task(	'css_admin',
			false,
			function() {
				gulp.src(config.css_admin)
				.pipe($.plumber({
					errorHandler: util.onError
				}))
				.pipe($.sass().on('error', util.onError))
				.pipe($.autoprefixer({
					cascade: false
				}))
				.pipe($.size({ title: 'LOG css_admin' }))
				.pipe( $.util.env.type === 'production' ? $.minifyCss() : $.util.noop())
				.pipe($.size({ title: 'LOG css_admin:min' }))
				.pipe(gulp.dest(paths.static.min.root + "/css/admin"));
			}
);
