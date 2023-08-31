## A simple CRUD Application for managing a person's details like name, address, contact number, etc created using Python, Django and Postgre SQL using Oauth Protocol.

## Note: Python 3.7 or above must be installed.

## Build
1. Clone the repo:
```
git clone https://github.com/sundramkush/Personal_Profile.git
```
2. Make a virtual environment and activate it:
* For Windows:
```
py -m venv myworld
```
```
myworld\Scripts\activate.bat
```
* For Unix/MacOS:
```
python3 -m venv myworld
```
```
source myworld/bin/activate
```
3. Installing the requirements using pip.
```
pip install -r requirements.txt
```
4. Installing  and Running the Database (Postgres) (Postgresql 15 Recommended)
* For Windows:
	* Download the Windows installer from [here](https://www.enterprisedb.com/downloads/postgres-postgresql-downloads) by following the steps from [postgresqltutorial-Windows](https://www.postgresqltutorial.com/postgresql-getting-started/install-postgresql/) to successfully install all the dependencies of the database server.
     
* For MacOS:
	* Download the macOS installer from [here](https://www.enterprisedb.com/downloads/postgres-postgresql-downloads) by following the steps from [postgresqltutorial-MacOS](https://www.postgresqltutorial.com/postgresql-getting-started/install-postgresql-macos/) to successfully install all the dependencies of the database server.
     
* For Unix:
	* Follow the steps [here](https://www.postgresqltutorial.com/postgresql-getting-started/install-postgresql-linux/) for Unix installation of Postgresql

* After completing the installation and setting up a Postgresql server, Create a database for the application to connect.
     
5. Configure the settings.py in the Personal_Profile folder with the details of the database configured before in the Databases section of the file after line 85:
```
   DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'xxxxxxxxxxx', // put the name of the database created here
        'USER': 'xxxxxxxxx',   // put the name of the superuser created while setting up the PostgreSQL server
        'HOST': 'localhost'  
    }
}
```

### Note: Make sure the database server is running to continue to the next steps.

## Run
1. To run the application, write this command inside the project directory and go to your browser to open [localhost page](http://127.0.0.1:8000/).
* For Windows:
```
py manage.py migrate
py manage.py runserver 
```
* For macOS/Linux:
```
python3 manage.py migrate
python3 manage.py runserver
```
2. To run the test suite:
* For Windows:
```
py manage.py test
```
* For macOS/Linux:
```
python3 manage.py test
```


