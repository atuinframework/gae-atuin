var p = {};

// ## main
p.main = {};
p.main.root = 'app';

// ## static
p.static = {};
p.static.root 	= p.main.root + '/static';

// ## src
// static/src
p.static.src = {};
p.static.src.root = p.static.root + '/src';

// static/src/css
p.static.src.css = {};
p.static.src.css.root = p.static.src.root + '/css';

// static/src/js
p.static.src.js = {};
p.static.src.js.root = p.static.src.root + '/js';

// static/src/img
p.static.src.img = {};
p.static.src.img.root = p.static.src.root + '/img';

// ## min
// static/min
p.static.min = {};
p.static.min.root = p.static.root + '/min';

// static/min/css
p.static.min.css = {};
p.static.min.css.root = p.static.min.root + '/css';

// static/min/js
p.static.min.js = {};
p.static.min.js.root = p.static.min.root + '/js';

// static/min/img
p.static.min.img = {};
p.static.min.img.root = p.static.min.root + '/img';

module.exports = p;
