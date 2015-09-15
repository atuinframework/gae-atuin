var p = {};

// main
p.main = {};
p.main.root = 'app';

// static
p.static = {};
p.static.root 	= p.main.root + '/static';

// static/dev
p.static.dev = {};
p.static.dev.root = p.static.root + '/dev';

// static/min
p.static.min = {};
p.static.min.root = p.static.root + '/min';
p.static.min.img = {};
p.static.min.img.root = p.static.min.root + '/img';


// static/src
p.static.src = {};
p.static.src.root = p.static.root + '/src';

//TODO min js css img


// static/src/css
p.static.src.css = {};
p.static.src.css.root = p.static.src.root + '/css';

// static/src/js
p.static.src.js = {};
p.static.src.js.root = p.static.src.root + '/js';

// static/src/img
p.static.src.img = {};
p.static.src.img.root = p.static.src.root + '/img';

module.exports = p;
