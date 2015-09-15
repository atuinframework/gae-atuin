paths = require('./paths.js');

config ={
	'css' : [
		paths.static.src.css.root + '/style.scss'	
	],
	'css_admin' : [
		paths.static.src.css.root + '/admin/style.scss'	
	],
	'js' : [
		paths.static.src.js.root + '/*.js'	
	],
	'js_admin' : [
		paths.static.src.js.root + '/admin/*.js'	
	],
	'img' : [
		paths.static.src.img.root + '/**/*.@(jpg|gif|png|svg)'
	]
}

module.exports = config;
