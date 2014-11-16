Job Tracker
===========

An app by [Derrick](http://derrickshowers.com/) and [Sarah](http://sarahlshowers.github.io/) Showers.

## Installation and configuration

There are a couple of quick steps to get this running on your machine (assumiung, of course, you're running OS X or certain flavors of Linux - sorry Windows peeps).

1. Some Initial Setup (make sure you have [Homebrew](http://brew.sh/) installed)

		$ brew install python
		$ brew install python3
		$ pip install virtualenv
		$ cd <whatever-you-want-to-put-this-thang>
		$ virtualenv job-tracker --no-site-packages -p /usr/local/bin/python3.4
		$ cd job-tracker
		$ git clone git@github.com:derrickshowers/job-tracker.git 

2. Active vitual env

        $ . bin/activate

3. Install dependencies

		$ cd job-tracker
		$ pip install -r requirements.txt

3. Start server

        $ python manage.py runserver

4. Navigate to [http://localhost:8000/](http://localhost:8000/).

*When finished, you probably want to type `deactivate` to exit the virtual envrionment*

## Structure

Most of the front end code lives in one of two places:

1. Markup: `jobtracker/templates`. Everything is broken up into 'app' specific directories. Django likes to split everything up into apps, for each module of the project. For instance, all markup related to the 'jobs' module is in `jobtracker/templates/jobs`. There is also a `common` directory for any base or reused markup.

2. Static Assets: All CSS, JS, and images are in `jobtracker/static`. If you need to include a new static file on any HTML page, put `{% load staticfiles %}` at the top of the page, and then something like `{% static 'css/my-css-file.css' %}` wherever it needs to go in the markup.

## Credentials and stuff

### Admin

The admin console is at [http://localhost:8000/admin](http://localhost:8000/admin).  
*Username*: theshowersfam  
*Password*: walterdog  
