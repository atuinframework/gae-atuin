# GAE Atuin v2 - A Flask web application skeleton.

This is the Google AppEngine version of [Atuin], a [Scalebox]'s Flask web application skeleton.


### Features included

 - The good famous Flask web framework
 - Babel
 - Google Auth support and decorators
 - js concatenation and minify (+ obfuscation)
 - SASS preprocessor
 - Image optimization
 - External libraries inclusion
 - Almost Everything managed by Gulp

 
## Development environment

#### What's required to execute it?

Just `docker-compose`.

To run local development environment:

```bash
docker-compose up
```


#### Docker containers

- **devenv** - Google CLoud SDK.
    
    - Run the local development server of GAE SDK 

- **tools** - Node.js & gulp tasks
    
    - To manage project's dependencies.
    - To handle project's static files (concatenate, minify and uglify).
    - To handle project's translations.
    - To prepare static files for deployment.


## Handle dependencies

When you run for the first time the GAE Atuin framework environment you have to install the python dependencies.
To do this, as the tasks to manage translations, you have to connect to the `atuin-tools` container.

1. With the development environment running, connect to the tools container.
```bash
docker exec -it tools sh
```
2. Then, use pip through the dedicated Gulp task to update them.
```bash
# To get the Gulp help
gulp

# Update dependecies
gulp update
```

Each time you change the `requirements.txt` file don't forget to run this update task.


## Translations

Flask-Babel is fully supported. [Official documentation]

#### To manage project translations:

1. With the development environment running, connect to the tools container.
```bash
docker exec -it tools sh
```
2. Many gulp tasks are available to extract, initialize, update and compile the project translated word.

```bash
# To get the Gulp help
gulp

# Manage translations
gulp translations[:extract|:update|:compile|:init]
```


## Deploy

### Before the deploy... don't forget to:

1. Check `app/config.py`
2. Check `app/version.py`
3. Check `app/app.yaml`
4. (Translation? Up to date?)
5. Minify, uglify and compress (production mode) the project's static files:

```bash
docker-compose run tools gulp prepare-deploy
```

### Deploy

[TODO docs]

1. To do the deploy use the `devenv` container.
```bash
$ docker-compose run --rm devenv bash
```

2. Authenticate with your account.
```bash
# gcloud auth login 'ACCOUNT'
```

3. Deploy the project.
```bash
# gcloud app deploy --project=<project-id> workspace/app/app.yaml
```


## Code conventions
 - `Admin` `_admin` at the end of name for admin variables
 - `.btnSave` `.btnNewWhatNew` `.normalContentCSSClass`
 - `form_nameofcontent.html` `modal_nameofcontent.html` the content type of the file is a prefix

[Atuin]: https://bitbucket.org/account/user/scalebox/projects/ATUIN
[Scalebox]: http://www.scalebox.it/
[Official documentation]: http://pythonhosted.org/Flask-Babel/
