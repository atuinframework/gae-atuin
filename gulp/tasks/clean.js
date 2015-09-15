'use strict';
var del = require('del'),
	gulp = require('gulp-help')(require('gulp')),
	paths = require('../paths.js');

gulp.task(	'clean',
			false,
			function () {
				del('./**/*.pyc');
				del('./**/*.pyo');
				del('./**/*.~');			
			}
);

gulp.task(	'clean:min',
			false,
			function () {
				return del(paths.static.min.root);
			}
);
