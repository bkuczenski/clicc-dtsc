# CLICC-DTSC Integration Project

The purpose of this project is to prototype one possible form of remote
user interaction with the CLiCC database in order to obtain information in
a semi-automated way.

The project implements a web service in
[django](https://docs.djangoproject.com/en/1.8/) that exposes a basic
schema of chemical properties and LCIA results.

![DTSC Collaboration](clicc-dtsc-Collaboration-Model.png)

## Database connection

The django server connects to the engineering database to store the website 
and user data.  To use the program you must edit the authentication settings 
(username and password) in `/src/clicc_dtsc/clicc_dtsc/my.cnf` to enable you 
to connect to the database server.

If you would like to use encryption you need to create a secret key in the 
location `/src/clicc_dtsc/clicc_dtsc/secret_key.txt` (untested).

## Running the Program

I used Eclipse with [PyDev](http://www.pydev.org) to run and test development. 
To run the program, change to the `src/clicc_dtsc` folder in a shell and run 

    $ python manage.py runserver

That will start the server.  Then you can connect to it on a web browser from 
your local machine using the address `http://localhost:8000`

## Valid Routes

The valid routes are defined in `src/clicc_dtsc/clicc_dtsc/urls.py` and include:

    http://localhost:8000/admin
    http://localhost:8000/api/modules
    http://localhost:8000/api/result
    http://localhost:8000/api/lciaresult
    http://localhost:8000/api/v1/chemical
    http://localhost:8000/api/v1/property
    http://localhost:8000/api/v1/product
    http://localhost:8000/api/v1/constituent
    http://localhost:8000/api/v1/application
    http://localhost:8000/api/v1/annotation

The admin credentials are configured at the time the admin site is first setup. 
The credentials for the current `engr` database are in the powerpoint file 
documenting the deployment.
