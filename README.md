# RSS-grabber
be the first one notified with the latest news.


## Technologies used
- Python 3.9
- Django 4.0
- Django Rest Framework 3.13
- Docker
- Git
- Celery
- Redis
- Simple JWT
- Swagger


## Installation
1- clone the project
```
git clone git@github.com:AliHosseinzadeh2000/RSS-grabber.git
```
2- rename '.env-sample' to '.env' and provide the required variables.

3- create a python virtual environment:
```
python -m venv venv
```
4- activate your venv
- on linux and mac:
  ```
    source venv/bin/activate
  ```
- on windows:
  ```
    venv/Scripts/activate
  ```
5- install dependencies
```
pip install -r requirements.txt
```
6- run a redis container on docker
```
docker run --name myredis -p 6379:6379 -d redis
```
7- run a celery worker in a seprated terminal tab
```
celery -b redis://localhost:6379 -A main.tasks worker -E -l INFO -P gevent -Q news
```
8- run celery beat in another tab:
```
celery -b redis://localhost:6379 -A main.tasks beat -l INFO
```
9- migrate the database:
```
python manage.py migrate
```
10- run the project:
```
python manage.py runserver
```


## Endpoints
Endpoints are available at [~:8000/swagger/](http://localhost:8000/swagger/)
