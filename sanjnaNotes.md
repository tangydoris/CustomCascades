#11/30 Notes
After talking with Chelsea, it appears that we should be doing everything commandwise inside of the virtual environment
I think is because you want to isolate your project's dependencies from your computer's technologies.
https://www.getfilecloud.com/blog/working-with-virtualenv-on-django-projects/
https://www.digitalocean.com/community/tutorials/how-to-install-and-use-postgresql-on-ubuntu-14-04
https://www.postgresql.org/docs/current/static/app-psql.html

So inside venv, I created an inital user who can login to the admin site
`(venv) $ python manage.py createsuperuser`
Username: admin
Email: admin@example.com
Password: hello123

After a couple hours, not only does the admin config work but I was able to reverse engineer Scalica to create a login system and posts page

To do's at this point:
Figure out how to default 127.0.0.1:8000/micro to just 127.0.0.1:8000
Able to log in and figure all that stuff out, which is good.

Now let's figure out how to get followers/find followers and then upload CSS documents

Display information relevant to project


#As of Day 2 (11/29)
Turns out, I had multiple versions of django, python, and postgres running therefore my computer continuously ran into errors in deploying the app.

After deleting all these versions, I started over and reinstalled only 1 instance of django, python, postgres... etc.

##Things to remember
If you are pip installing anything new, remember to commit it to the requirements.txt file with the following command
`pip freeze > requirements.txt`<br />
Then you can commit it to github

When you do a `git pull`, open the virtual environment by:
1) delete any past instance of virtual environments by:<br />
`$ deactivate`<br />
`$ rm -r venv`<br />
`$ virtualenv venv`<br />
`$ . venv/bin/activate`<br />
`$ pip install -r requirements.txt`<br />

To run the server: `python manage.py runserver`<br />
When I first did this, I got an error message, that led me to configure the postgres. I had to create the database and user on postgres (got help from the postgres app) based off what was in my settings.py. My process went as such:

1) CMD+T to open a new tab in terminal window
2) open psql by
`$ psql`<br />
3) type in the following commands into the terminal window
`CREATE ROLE testuser WITH LOGIN SUPERUSER PASSWORD 'password';`<br />
`CREATE DATABASE testdatabase WITH OWNER=testuser;`<br />
**Please note that this is not for production (unsafe)!**
This is just how I was able to get the initial app off the ground<br />

[The URL to assist with Postgresql DB commands](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-postgresql-on-ubuntu-14-04)

#As of Day 1 (11/28)
#Download Postgres
`$ brew install postgresql`
'$ pip install psycopg2`

The following are all terminal commands
#Creating the Database
Initially, with help from https://www.digitalocean.com/community/tutorials/how-to-use-postgresql-with-your-django-application-on-ubuntu-14-04

`CREATE DATABASE customcascades;`
`CREATE USER customcascadesuser WITH PASSWORD 'password';`
`ALTER ROLE customcascadesuser SET client_encoding TO 'utf8';`
`ALTER ROLE customcascadesuser SET default_transaction_isolation TO 'read committed';`
`ALTER ROLE customcascadesuser SET timezone to 'UTC';`

Give our DB user access rights to the DB we have just created
`GRANT ALL PRIVILEGES ON DATABASE customcascades TO customcascadesuser;`
[Markdown language helper] (https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet#emphasis)


