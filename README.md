<div align="center">
  <img src="https://4.bp.blogspot.com/-gCN_J_hrefY/WGkMWk_mitI/AAAAAAAAIWg/3TSASbVNJHIhEUgOKgREM8Ayvn918u1JQCLcB/s1600/sih2017-home.jpg"><br><br>
</div>

### What is this repository for? ###

* This repository showcases the work done by [Team Extrapolate](mailto:extrapolate@googlegroups.com), [Winners Smart India Hackathon 2017](https://innovate.mygov.in/sih2017/ "Smart India Hackathon"), under Ministry of HRD, Government of India, for the project that was awarded to the Team, by [All India Council for Technical Education, Government of India](https://www.aicte-india.org/, "All India Council for Technical Education").

### How do I get set up? ###

#### Summary of set up
* **Always work in a virtual environment**, install virtual environment from `https://virtualenv.pypa.io/en/stable/` .
* Download virtual environment for Python3.x .
* To run the project, go to the root directory of the project run `virtualenv env`
* Then install activate the virtual environment, using `source env/bin/activate`
* Install the dependencies by `pip3 install -r requirements.txt`
* Install PostgreSQL, as the relational database.
   - Create user: `sih17_admin`
   - Create db: `sih17`
   - Add password to db: `sih17winners`
   - For more follow this [blog](https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-ubuntu-16-04, "How to setup the database")
* If this the first time installation of the project, run `python3 manage.py migrate`
* To run the server `python3 manage.py runserver`
* To deactivate the virtual environment `deactivate`
* [Deployment instructions](https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-ubuntu-16-04, "How to deploy?")

### Contact ###

* For queries, you can reach us out at: [`extrapolate@googlegroups.com`](maitlo:extrapolate@googlegroups.com)
