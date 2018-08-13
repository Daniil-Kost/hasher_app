**Welcome to the Hasher Test App public repository!**

**Installation**
1) Setup and activate your python2.7 virtualenv
2) Clone project from GitHub: `git clone https://github.com/Daniil-Kost/hasher_app.git`
3) Go to the project directory and install requirements: `pip install -r requirements.txt`

4) Create PostgreSQL DB with credentials: name: demo; user: demouser; password: password (
or with anything credentials and change settings.py DATABASES dict )

5) Setup DB with following command`python manage.py migrate`

6) Add project tables to the DB. Run the following command: `python manage.py makemigrations`

7) Synchronize last changes in the DB:  `python manage.py migrate` 

8) Fill DB by following command: `python manage.py fill_db`

9) Run server `python manage.py runsever`

10) Open http://localhost:8000/

**IMPORTANT**
_This project has some bugs - it will be fix in future_

**WARNING**
_This code work correctly only on the server. If you run app localy - you get
    # wrong (local) ip address: "127.0.0.1"_
