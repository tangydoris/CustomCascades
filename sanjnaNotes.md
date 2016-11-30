#As of Day 2 (11/29)
Turns out, I had multiple versions of django, python, and postgres running therefore my computer continuously ran into errors in deploying the app.

After deleting all these versions, I started over and reinstalled only 1 instance of django, python, postgres... etc.

##Things to remember
If you are pip installing anything new, remember to commit it to the requirements.txt file with the following command
`pip freeze > requirements.txt`
Then you can commit it to github

When you do a `git pull`, open the virtual environment by:
1) delete any past instance of virtual environments by:
`$ deactivate`
`$ rm -r venv`
`$ virtualenv venv`
`$ . venv/bin/activate`
`$ pip install -r requirements.txt`

To run the server: `python manage.py runserver`
When I first did this, I got an error message, that led me to configure the postgres. I had to create the database and user on postgres (got help from the postgres app) based off what was in my settings.py. My process went as such:

1) CMD+T to open a new tab in terminal window
2) open psql by
`$ psql`
3) type in the following commands into the terminal window
`CREATE ROLE testuser WITH LOGIN SUPERUSER PASSWORD 'password';`
`CREATE DATABASE testdatabase WITH OWNER=testuser;`
**Please note that this is not for production (unsafe)!**
This is just how I was able to get the initial app off the ground

[a link](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-postgresql-on-ubuntu-14-04)

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



