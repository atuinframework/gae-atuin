'use strict';
var gulp = require('gulp-help')(require('gulp')),
	$ = require('gulp-load-plugins')(),
	config = require('../config.js'),
	mkdirs = require('mkdirs');
	
gulp.task(	'run',
			'Run development server.',
			function() {
				mkdirs(config.tmp.datastore_db);
				gulp.src('dev.sh')
					.pipe($.start( [{
						match: /dev.sh$/,
						cmd: 'dev_appserver.py --storage_path=tmp/datastore app'
					}]));
			}
);

gulp.task(	'update',
			'Updates Python requirements.',
			function() {
				$.sequence('update:pip')();
			}
);

gulp.task(	'monitor',
			'Real time check for css and js.',
			function() {
				$.sequence(['css', 'css_admin', 'js', 'js_admin', 'img'], 'watch')();
			}
);

gulp.task(	'deploy',
			'Deploy on gae.',
			function() {
				$.util.log('TODO!');
			}
);
