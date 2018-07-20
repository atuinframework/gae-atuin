
# GAE Atuin Web Framework - A Flask web application skeleton

This is the Google AppEngine version of [Atuin Web Framework], a [Scalebox]'s 
Flask web application skeleton. This porting is designed to be deployed on 
[Google App Engine] and to use the [Google Datastore].


### Features

- The good famous [Flask] web framework
- i18n with [Babel]
- Google Auth support and decorators
- The [atuin-tools] development environment for
	
	- SASS preprocessing
	- CSS concatenation and minification
	- JS concatenation, minification and obfuscation
	- Images optimization
	- Translations management (extraction, compilation)
	- Pre-deploy preparation task
	- Deploy procedure


### Requirements

- `docker`
- `docker-compose`


###  Quick start

```bash
git clone git@github.com:atuinframework/gae-atuin.git

cd gae-atuin

# install dependencies
docker-compose run --rm tools gulp update

docker-compose up
```

###  Links

- [GAE Atuin documentation]
- [Atuin tools documentation]
	
	Look at this documentation for:
		- Static files management (CSS, JS, images)
		- Translations handling
		- Deploy procedure
	
- [Atuin Web Framework]


[Atuin Web Framework]: https://github.com/atuinframework
[Scalebox]: http://www.scalebox.it/
[Google App Engine]: https://cloud.google.com/appengine/
[Google Datastore]: https://cloud.google.com/datastore/
[Flask]: https://github.com/pallets/flask
[Babel]: http://babel.pocoo.org/en/latest/
[atuin-tools]: https://github.com/atuinframework/atuin-tools
[GAE Atuin documentation]: http://gae-atuin.rtfd.io/
[Atuin tools documentation]: http://atuin-tools.rtfd.io/
