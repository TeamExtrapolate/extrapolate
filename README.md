# README #



### What is this repository for? ###

* This is project for Team Extrapolate `extrapolate@googlegroups.com`, [Winners Smart India Hackathon 2017](https://innovate.mygov.in/sih2017/ "Smart India Hackathon"), under Ministry of HRD, Government of India.
* V1.0

### How do I get set up? ###

#### Summary of set up
* Always work in a virtual environment, install virtual environment from `https://virtualenv.pypa.io/en/stable/` .
* Download virtual environment for Python3.x .
* To run the project, go to the root directory of the project run `virtualenv env`
* Then install activate the virtual environment, using `source env/bin/activate`
* Install the dependencies by `pip3 install -r requirements.txt`
* Install PostgreSQL, as the relational database.
   - Create user: `sih17_admin`
   - Create db: `sih17`
   - Add password to db: `sih17winners`
   - Fo more follow this [blog](https://www.digitalocean.com/community/tutorials/how-to-serve-django-applications-with-apache-and-mod_wsgi-on-ubuntu-14-04)
* If this the first time installation of the project, run `python3 manage.py migrate`
* To run the server `python3 manage.py runserver`
* To deactivate the virtual environment `deactivate`
* Configuration
* Dependencies
* Database configuration.
* How to run tests
* Deployment instructions

### Contribution guidelines ###
* Always work in a branch.
* Writing tests
* Code review
* Other guidelines

### Who do I talk to? ###

* Repo owner or admin 
* Mail at `mailbag.akshay@gmail.com`
* Other community or team contact
