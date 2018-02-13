
# GAE Atuin Web Framework - A Flask web application skeleton.

This is the Google AppEngine version of [Atuin Web Framework], a [Scalebox]'s 
Flask web application skeleton.


### Features included

 - The good famous Flask web framework
 - Babel
 - Google Auth support and decorators
 - js concatenation and minification (+ obfuscation)
 - SASS preprocessor
 - Image optimization
 - Automatic dependencies management

 
### Requirements

- `docker`
- `docker-compose`


### Initial setup

The firs time you run the GAE Atuin framework it is necessary to
install the python dependencies of the project:

1. Connect to the atuin-gulp container
```bash
docker-compose run --rm atuin-gulp sh
```
2. Run the Gulp task to update/install dependencies
```bash
gulp update
```

Each time you change the the project dependencies update them with this command.


### How to run the project

```bash
docker-compose up
```


### Language translations

[Flask-Babel] is fully supported.

#### Translations management

1. Connect to the atuin-gulp container
```bash
docker-compose run --rm atuin-gulp sh
```
2. Many gulp tasks are available to extract, initialize, update and compile the 
project translations.

```bash
# To get the Gulp help
gulp

# Manage translations
gulp translations[:extract|:update|:compile|:init]
```


### Deployment

Quick reminder before to do the deployment:

1. Check `app/config.py`
2. Check `app/version.py`
3. Check `app/app.yaml`
4. [Update translations]
5. Optimize the project's static files for production:

```bash
docker-compose run --rm atuin-gulp gulp prepare-deploy
```

#### Deploy over GAE through the devenv container

1. Connect to the devenv container
```bash
docker-compose run --rm devenv sh
```

2. Do the login
```bash
gcloud auth login <gcloud account email>
```

3. Deploy
```bash
gcloud app deploy --project=<project-id> /workspace/app/app.yaml
```


### Code conventions
 - `Admin` `_admin` at the end of name for admin variables
 - `.btnSave` `.btnNewWhatNew` `.normalContentCSSClass`
 - `form_nameofcontent.html` `modal_nameofcontent.html` the content type of the
 file is a prefix

### More on the docker containers

- **devenv** the [GAE Atuin development environment]
- **atuin-gulp** the [CASE] tool [Atuin Gulp]

    - To manage project's dependencies.
    - To handle project's static files (concatenate, minify and uglify).
    - To handle project's translations.
    - To prepare static files for deployment.

[Atuin Web Framework]: https://github.com/atuinframework
[Scalebox]: http://www.scalebox.it/
[Flask-Babel]: http://pythonhosted.org/Flask-Babel/
[GAE Atuin development environment]: https://github.com/atuinframework/gae-atuin-devenv
[CASE]: https://en.wikipedia.org/wiki/Computer-aided_software_engineering
[Atuin Gulp]: https://github.com/atuinframework/atuin-gulp