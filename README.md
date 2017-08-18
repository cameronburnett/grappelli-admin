
TO RUN SITE LOCALLY VIA COMMAND LINE: 
	1) navigate to the admin-final folder
	2) run $ py manage.py makemigrations, then $ py manage.py migrate. this will ensure that the database models are consistent with the models.py file. 
	3) finally, run $ py manage.py runserver. it will automatically run on local host 8000. use Chrome to access the site.

BEFORE DEPLOYING: 
	--- Change DEBUG to False in settings.py 
		--- NOTE: setting DEBUG to False and then running the app on a local host will break the Grappelli admin interface. keep DEBUG = True while in development (working on local server). change it to False only when ready to deploy. it will reduce the number of db queries and improve the performance of the site.
	--- Change CSRF_COOKIE_SECURE to True in settings.py 
	--- Remove SECRET_KEY from settings.py file. Set the secret key as an environment variable on the production 
	environment and then retrieve the variable using os.environ.get() in settings.py. i.e. SECRET_KEY = os.environ.get('SECRET_KEY')
	--- Plug into the MySQL database whose information is commmented out on the settings.py file
	--- Set SESSION_COOKIE_SECURE to True to avoid transmitting the session cookie over HTTP accidentally 
	--- Setting CONN_MAX_AGE to None enables persistent database connections that result in a nice speed-up when connecting to the database accounts. This can help a lot on virtualized hosts with limited network performance.
	