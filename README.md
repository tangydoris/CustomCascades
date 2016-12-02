# CustomCascades
NYU Large Scale Web Applications Fall 2016 Semester Final Project

###To Do's:
Doris: figure out how to find and upload CSS documents --> make those models

Display information relevant to project

###Have Dones: 
Have started a Django project within our CustomCascades directory with command
```django-admin startproject CustomCascades```

##Configuring Django Database Settings
###System Requirements: 
This project uses:
`Django Version 1.10`
`Python 2.7`
`virtualenv`

Use the `requirements.txt` file for what is to be installed in the `venv`
You can install these requirements by `$ pip install -r requirements.txt` once you are in your virtual environments
## For initial download on your engine
`$ brew install postgresql`


## To Run This Project On Your Engine
1) Git clone the project to your system
2) Delete any previous instances of virtualenv on your computer by saying: <br />
`$ deactivate`<br />
`$ rm -r venv`<br />
3) Start a new instance of virtualenv by :  <br />
`$ virtualenv venv`<br />
`$ . venv/bin/activate`<br />
4) Install system requirements for the virtualenv by: <br />
`$ pip install -r requirements.txt`<br />
If you run into errors, it might be because this command sucks. You might have to manually install django. <br />
In the event that you have to manually install any commands via pip, please do :
`pip freeze > requirements.txt`<br />
before you commit and/or git pull anything new.

5) run by writing `(venv) $ python manage.py runserver`

## Running migrations
After you git pull, make sure to run migrations
$ python manage.py makemigrations css_app
$ python manage.py migrate

## Create super user for admin console
$ python manage.py createsuperuser

This automatically asks you to enter username, admin, and password which you can use for the admin console which is at '/admin'