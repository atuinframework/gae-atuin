'use strict';
var gulp = require('gulp-help')(require('gulp')),
	requireDir = require('require-dir')('./gulp/tasks'),
	paths = require('./gulp/paths.js'),
	config = require('./gulp/config.js'),
	$ = require('gulp-load-plugins')();
	
gulp.task(	'default',
			'Shows the available tasks',
			function () {
				$.util.log('\n'+
					$.util.colors.green('GULP TASKS') + '\n\t' +
					
					// default | help
					$.util.colors.yellow('default | help') + '\n\t\t' +
					'Shows the available tasks\n\n\t' +
					
					// run
					$.util.colors.yellow('run') + '\n' +
					'\t\tRun development server.\n\t\tGulp run the dev_appserv.py of gae SDK and set env variables.\n\n\t' +
					
					// update
					$.util.colors.yellow('update') + '\n\t\t' +
					'Management of the development environment.\n\t\tIt checks that all dependencies are satisfied, initializes the env packages and update them.\n\n\t' +
					
					// monitor
					$.util.colors.yellow('monitor [--type production]') + '\n\t\t' +
					'Real time check for css and js.\n\t\tIt handles errors and rebuilds the minified and compiled files.\n\t\t' +
					$.util.colors.magenta('--type production') + 'compress css and obfuscate js.\n\n\t' +
					
					// deploy
					$.util.colors.yellow('deploy') + '\n\t\t' +
					'Deploy on gae.\n\n\t' +
					
					// clean
					$.util.colors.yellow('clean[:min|:css|:js|:img]') + '\n\t\t' +
					'Cleans files.\n\t\tFrom all project clean: *.pyc *.pyo *.~\n\t\t' +
					$.util.colors.magenta(':min') +	' Clean all minified fiels  ' 	+ $.util.colors.green(paths.static.min.root) 	 + '\n\t\t' +
					$.util.colors.magenta(':css') + ' Clean minified CSS  ' 		+ $.util.colors.green(config.min.css) + '\n\t\t' +
					$.util.colors.magenta(':js')  + ' Clean minified JS  ' 			+ $.util.colors.green(config.min.js)  + '\n\t\t' +
					$.util.colors.magenta(':img') + ' Clean optimized img  ' 		+ $.util.colors.green(config.min.img) + '\n'
				);
			}
);
