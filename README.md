## Setup
Create environment
```
python3 -m venv env
source env/bin/activate
```
Install Dependencies
```
pip install -r requirements.txt
sudo apt install gdal-bin libgdal-dev
sudo apt install python3-gdal
```


Setup DB
```
DATABASES  = {
	'default': {
	'ENGINE': 'django.contrib.gis.db.backends.postgis',
	'NAME': 'DBNAME',
	'USER': 'USERNAME',
	'PASSWORD': 'PASSWORD',
	'HOST': 'localhost',
	'PORT': '5432'
	}
}
```
Migrations
```
python manage.py migrate
```
Create user
```
python manage.py createsuperuser
```

## Run
```
python manage.py runserver
```
## Signup

http://127.0.0.1:8000/accounts/signup/

