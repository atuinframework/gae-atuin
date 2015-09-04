var gulp  = require('gulp'),
	gutil = require('gulp-util'),
	sourcemaps = require('gulp-sourcemaps'),
	concat = require('gulp-concat'),
	uglify = require('gulp-uglify');

// default task
gulp.task('default', function() {
	return gutil.log('Gulp default');
});

gulp.task('build-pratiche-js', function() {
	return gulp.src('static/js/admin/pratiche-src/*.js')
		//.pipe(sourcemaps.init())
		.pipe(concat('pratiche.js'))
		//only uglify if gulp is ran with '--type production'
		.pipe(gutil.env.type === 'production' ? uglify({mangle:true}) : gutil.noop()) 
		//.pipe(sourcemaps.write())
		.pipe(gulp.dest('static/js/admin'));
});

gulp.task('build-anagrafiche-js', function() {
	return gulp.src('static/js/admin/anagrafiche-src/*.js')
		//.pipe(sourcemaps.init())
		.pipe(concat('anagrafiche.js'))
		//only uglify if gulp is ran with '--type production'
		.pipe(gutil.env.type === 'production' ? uglify({mangle:true}) : gutil.noop()) 
		//.pipe(sourcemaps.write())
		.pipe(gulp.dest('static/js/admin'));
});


gulp.task('watch', function () {
	gulp.watch('static/js/admin/pratiche-src/*.js', ['build-pratiche-js']);
	gulp.watch('static/js/admin/anagrafiche-src/*.js', ['build-anagrafiche-js']);
});
