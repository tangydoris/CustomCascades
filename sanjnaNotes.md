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



