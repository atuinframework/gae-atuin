## Project libs
These libraries will be minified and optimized for better performance on page loading.

Attention: `public libs` are distinguished from `admin libs`

### To include lib css, in `/static/src/style.scss` add
```scss
@import 'lib_css';
```

### To include lib js, in `/static/libs/libs.json`
```json
libs = {
	js:[
		'path_for_lib/lib.js'
	],
	admin:{
		js:[
			'path_for_admin_lib/lib.js'
		]
	}
}
```

### Destinations
Concatenated and minified javascript:

- **Public libraries** `/static/min/libs/js/all.js`
- **Admin libraries** `/static/min/libs/js/admin/all.js`
