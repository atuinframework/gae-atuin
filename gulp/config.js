paths = require('./paths.js');

config ={
	'src' : {
		'css' 		: [ paths.static.src.css.root + '/style.scss'	],
		'css_admin' : [ paths.static.src.css.root + '/admin/style.scss'	],
		'js' 		: [ paths.static.src.js.root + '/*.js'	],
		'js_admin'	: [ paths.static.src.js.root + '/admin/*.js' ],
		'img' 		: [ paths.static.src.img.root + '/**/*.@(jpg|gif|png|svg)' ]
	},
	'min' : {
		'css' 		: paths.static.min.css.root,
		'css_admin' : paths.static.min.css.root + '/admin',
		'js' 		: paths.static.min.js.root,
		'js_admin'  : paths.static.min.js.root + '/admin',
		'img' 		: paths.static.min.img.root
	},
	'lib' : paths.lib.root
}

module.exports = config;
