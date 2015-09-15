'use strict';
var gulp = require('gulp-help')(require('gulp')),
	$ = require('gulp-load-plugins')(),
	paths = require('../paths'),
	path = require('path'),
	del = require('del');

gulp.task(	'watch',
			false,
			function() {
				gulp.watch(paths.static.src.root + '/css/*', ['css']);
				gulp.watch(paths.static.src.root + '/css/admin/*', ['css_admin']);
				gulp.watch(paths.static.src.root + '/js/*', ['js']);
				gulp.watch(paths.static.src.root + '/js/admin/*', ['js_admin']);
				var watchImg = gulp.watch(paths.static.src.root + '/img/*', ['img']);
				watchImg.on('change', function(ev){
					if (ev.type==='deleted') {
						del( path.relative('./', ev.path).replace(paths.static.src.img.root, paths.static.min.img.root) );
					}
				});
			}
);
