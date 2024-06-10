## test-dashboard-store

Create api to resolve an store dashboard

## How to setup

## Requirements

    1. Docker version 26.00 or greter
    2. Python version 3.12 

## Local Development

  1. Copy and rename .env.enxample to .env
  2. Build development container (running on terminal):

    $ docker-compose -f docker-compose.yml up -d --build

  3. To run all migrations

    $ python manage.py migrate
  
  4. Cerate a user in db since docker

    $  python manage.py createsuperuser
  
  5. detect changes in  models

    $ python manage.py makemigrations

## Documentation

  The structor off project each module or app is a package to return especific endpoints and each contain:
  
    - dto: Data that use to manipulate the request in the app
    - migrations: Data migration in db
    - models: The models and repositories to call and manipulate the db
    - response: Data that return the endpoint
    - serializers: is used as validator
    - use_cases: The process to execute especific action in app

