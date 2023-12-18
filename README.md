# People Grouping

Django based Webapp tool which groups people living at identical addresses !

## Table of Contents

- [Features](#features)
- [Installation](#QuickStart)
- [Usage](#usage)
- [Libraries](#libraries)

## Features

All input data is saved in the SQLite database, all entries are unique pairs of name and address. 
All names in the database are grouped based on identical addresses entered for every name. The resulting list of names is sorted alphabetically.

Key Features are:

- A .csv file upload input
- A direct text input on the UI
- A .txt file export output
- Data reset

## QuickStart

## Local Development Environment

```bash
# installation command
$ git clone https://github.com/vmiroslav/people_grouping.git
$ cd people_grouping
$ python -m venv .
$ pip install -r requirements.txt
$ python manage.py migrate

```

## Usage

## Runing app in docker

```bash

$ cd people_grouping
$ docker-compose up -d  --build

```

## Runing on Local Environment

```bash

$ cd people_grouping
$ source bin/activate
$ python manage.py runserver 0.0.0.0:80

```


## Libraries
- [Django](https://www.djangoproject.com/) - Web framework for perfectionists with deadlines.
- [pandas](https://pandas.pydata.org/) - Powerful data manipulation library for Python.
- [django-bootstrap-v](https://github.com/dyve/django-bootstrap-v) - Django app for integrating Bootstrap with your project.
- [fuzzywuzzy](https://github.com/seatgeek/fuzzywuzzy) - Fuzzy string matching library for Python.