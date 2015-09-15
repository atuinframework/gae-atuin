'use strict';
var gulp = require('gulp-help')(require('gulp')),
	requireDir = require('require-dir')('./gulp/tasks'),
	$ = require('gulp-load-plugins')();
	
gulp.task(	'default',
			'Shows the available tasks',
			function () {
				$.util.log(
"\n",
$.util.colors.green('GULP TASKS\n'),
	"\t", $.util.colors.yellow('default | help\n'),
		"\t\t\Shows the available tasks\n\n",
		
	"\t", $.util.colors.yellow('run\n'),
		"\t\t\Run development server.\n\t\tGulp run the dev_appserv.py of gae SDK and set env variables.\n\n",
	
	"\t", $.util.colors.yellow('update\n'),
		"\t\t\Management of the development environment.\n\t\tIt checks that all dependencies are satisfied, initializes the env packages and update them.\n\n",
		
	"\t", $.util.colors.yellow('monitor\n'),
		"\t\t\Real time check for css and js.\n\t\tIt handles errors and rebuilds the minified and compiled files.\n\n",
	
	"\t", $.util.colors.yellow('deploy\n'),
		"\t\t\Deploy on gae.\n"
			
				);
			}
);
