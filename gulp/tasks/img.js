'use strict';
var gulp = require('gulp-help')(require('gulp')),
	$ = require('gulp-load-plugins')(),
	config = require('../config.js'),
	paths = require('../paths.js'),
	util = require('../util.js'),
	changed = require('gulp-changed');	

// public and admin specific
gulp.task(	'img',
			false,
			function() {
				return gulp.src(config.img)
						.pipe(changed(paths.static.min.root + "/img"))
						.pipe($.imagemin({
							progressive: true,
							svgoPlugins: [{removeViewBox: false}]
						}))
						.pipe(gulp.dest(paths.static.min.root + "/img"));
			}
);
