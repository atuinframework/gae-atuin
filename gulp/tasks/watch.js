'use strict';
var gulp = require('gulp-help')(require('gulp')),
	$ = require('gulp-load-plugins')(),
	paths = require('../paths'),
	path = require('path'),
	del = require('del');

gulp.task(	'watch',
			false,
			function() {
				gulp.watch(paths.static.src.css.root + '/*', ['css']);
				gulp.watch(paths.static.src.css.root + '/admin/*', ['css_admin']);
				gulp.watch(paths.static.src.js.root + '/*', ['js']);
				gulp.watch(paths.static.src.js.root + '/admin/*', ['js_admin']);
				var watchImg = gulp.watch(paths.static.src.img.root + '/**', ['img']);
				watchImg.on('change', function(ev){
					if (ev.type==='deleted') {
						del( path.relative('./', ev.path).replace(paths.static.src.img.root, paths.static.min.img.root) );
					}
				});
			}
);
