Simple Implementation of logistics flow
---

We have separate APIs for all the states so that if we want to add more functionalities to each states in future.

#### Requirements
```sh
1. Python 3.5
2. Django 2.0
3. PostgresSQL 9.6
```

### Create Virtual Environment
Follow instructions at: *http://pypi.python.org/pypi/virtualenv*

### Install Requirements
```sh
pip install -r requirements/base.txt

```

### Run Migrations
```sh
python manage.py migrate
python manage.py loaddata initial_data
```

### Run Server
```sh
python manage.py runserver
```
