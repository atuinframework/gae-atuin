# GAE - Flask - Atuin

Atuin is Scalebox's Flask web application skeleton, Google AppEngine version

## Package requirements:

 - Google AppEngine SDK in /usr/local/google_appengine
 - nodejs and npm

## Features included

 - The good famous Flask web framework
 - Babel
 - Google Auth support and decorators
 - js concatenation and minify (+ obfuscation)
 - SASS preprocessor
 - Image optimization
 - External libraries inclusion
 - Almost Everything managed by Gulp

## Installation

From the project directory:

```bash
	npm install -g gulp
	gulp update
```

## Launch development environment

Suggestion use **two** terminal window for:
```bash
    gulp run
```
```bash
    gulp monitor
```

## Gulp tasks

 - `gulp`
   **help**
   Shows the available tasks

 - `gulp run`
   **run development server**
   Gulp run the dev_appserv.py of gae SDK and set env variables

 - `gulp update`
    **management of the development environment**
    It checks that all dependencies are satisfied, initializes the env packages and update them

 - `gulp monitor [--type production]`
	**real time check for css and js**
	It handles errors and rebuilds the minified and compiled files
	`--type production` compress css and obfuscate js

 - `gulp deploy`
   **deploy**

## Translations

Flask-Babel is fully supported. [Official documentation](http://pythonhosted.org/Flask-Babel/)


## Other tools

... docs in progress ...


## TODO

 * Authentication abstractions
 * Cache abstractions
