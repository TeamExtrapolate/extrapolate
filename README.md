<div align="center">
  <img src="https://4.bp.blogspot.com/-gCN_J_hrefY/WGkMWk_mitI/AAAAAAAAIWg/3TSASbVNJHIhEUgOKgREM8Ayvn918u1JQCLcB/s1600/sih2017-home.jpg"><br><br>
</div>

Smart India Hackathon, 2017, was orgarnized jointly by Ministry of Human Resource Development, All India Council for Technical Education (AICTE), Inter Institutional Inclusive Innovation Center (i4C), and Persistent Systems, as a unique initiative to identify new and disruptive digital technology innovations for solving the challenges faced by our country, India.

### What is this repository for? ###

This repository showcases the work done by [Team Extrapolate](mailto:extrapolate@googlegroups.com), [Winners Smart India Hackathon 2017](https://innovate.mygov.in/sih2017/ "Smart India Hackathon"), for the project that was awarded to them by the [All India Council for Technical Education, Government of India](https://www.aicte-india.org/, "All India Council for Technical Education"), after securing the first position in Smart India Hackathon'17 under the AICTE.

### Project Details ###

The process entailed extracting information from the unprocessed data AICTE collects from Institutes across the country to find useful insights. The generated plots are being presented in the form of a web application.

### How to set up this project in your local machine? ###

#### Summary of set up
* **Always work in a virtual environment**, install virtual environment from `https://virtualenv.pypa.io/en/stable/` .
* Install **pip** by typing `curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py` and then typing `python3 get-pip.py`, to install **pip** for Python3.x
* Download and install virtual environment for Python3.x, by typing `pip install virtualenv`
* To run the project, go to the root directory of the project run `virtualenv env`
* Then install activate the virtual environment, using `source env/bin/activate`
* Install the dependencies by `pip3 install -r requirements.txt`
* [Install and configure PostgreSQL](https://github.com/sominwadhwa/extrapolate/wiki/PostGreSQL-installation), as the relational database.
* For more follow this [blog](https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-ubuntu-16-04, "How to setup the database")
* If you are configuring the project for the very first and all the database setup steps have been implemented successsfully please run the following to populate the relational db schema to the database created, type `python3 manage.py migrate`
* To run the server `python3 manage.py runserver`
* To deactivate the virtual environment `deactivate`
* [Deployment instructions](https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-ubuntu-16-04 "How to deploy?")

### Contact ###

* For queries, you can reach us out at: [`extrapolate@googlegroups.com`](maitlo:extrapolate@googlegroups.com)
