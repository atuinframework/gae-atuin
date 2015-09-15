'use strict';
var gulp = require('gulp-help')(require('gulp')),
	$ = require('gulp-load-plugins')(),
	config = require('../config.js'),
	paths = require('../paths.js'),
	util = require('../util.js'),
	jpegtran = require('imagemin-jpegtran'),
	pngquant = require('imagemin-pngquant'),
	gifsicle = require('imagemin-gifsicle'),
	svgo = require('imagemin-svgo');	

// public
gulp.task(	'img',
			false,
			function() {
				gulp.src(config.img)
				.pipe($.imagemin({
					progressive: true,
					svgoPlugins: [{removeViewBox: false}],
					use: [
						jpegtran({progressive: true}), //, arithmetic: true}),
						pngquant({progressive: true})
						  ]
				}))
				.pipe(gulp.dest(paths.static.min.root + "/img"));
				/*
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
				*/
			}
);

// admin specific
gulp.task(	'img_admin',
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
