'use strict';
var del = require('del'),
	gulp = require('gulp-help')(require('gulp')),
	paths = require('../paths.js');

gulp.task(	'clean',
			'From all project clean: *.pyc *.pyo *.~',
			function () {
				del('./**/*.pyc');
				del('./**/*.pyo');
				del('./**/*.~');			
			}
);

gulp.task(	'clean:min',
			'Clean all minified fiels, dir: ' + paths.static.min.root,
			function () {
				return del(paths.static.min.root);
			}
);

gulp.task(	'clean:css',
			'Clean minified CSS, dir: ' + paths.static.min.css.root,
			function () {
				return del(paths.static.min.css.root);
			}
);

gulp.task(	'clean:js',
			'Clean minified JS, dir: ' + paths.static.min.js.root,
			function () {
				return del(paths.static.min.js.root);
			}
);

gulp.task(	'clean:img',
			'Clean optimized img, dir: ' + paths.static.min.img.root,
			function () {
				return del(paths.static.min.img.root);
			}
);
