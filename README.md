
## Coursework 6 - Todolist

Backend for task-tracking application

### Stack

- django - backend
- postgresql - database
- development requirements are specified in todolist/requirements.txt

### Features

1. Authentication and User (core app):
   - VK Oauth
   - basic django authentication
   - profile update
   - password change
2. Main interface (goals app):
   - basic CRUD with filters and sorting: boards, goals, categories, comments
   - user can view items related to the boards he's member of (owner, writer or reader)
   - user can create categories, goals, comments only if he's owner/writer of the related board
   - user can update, delete only if he's owner/writer of the related board
   - user can update, delete only his comments
   - when board, category is marked as is_deleted, all child categoris, goals are also marked as is_deleted
3. Telegram bot (bot app):
   - user need to verify identity using verification code
   - user could view and create goals
   - bot telegram username: @TodolistFromSpaceBot

## How to launch project in development environment

1. Create virtual environment
2. Install dependencies from requirements.txt
   - `pip install -r todolist/requirements.txt`
3. Set environment variables in .env file
   - create .env file in todolist folder
   - you can copy the default variables from todolist/.env.example
4. Launch database from deploy folder
   - `cd deploy`
   - `docker compose --env-file ../todolist/.env -f docker-compose.yaml up -d`
5. Make migrations from todolist folder
   - `cd todolist`
   - `./manage.py makemigraitons`
   - `./manage.py migrate`
6. Launch project
   - `./manage.py runserver`

#### Accessing admin site

1. Create admin-user
   - `./manage.py createsuperuser`
   - set values and required fields
2. Access admin site at http://127.0.0.1:8000/admin/

## How to launch project in development with Docker-compose

1. Create .docker_env file in deploy folder:
   - you can copy the default variables from todolist/.env.example
   - make sure to set DB_HOST to `db` which is a container name
2. Use docker-compose.yaml from within deploy folder
   - `cd deploy`
   - `docker-compose up -d`
3. The following would be done:
   - postgresql container would start
   - migrations would apply
   - api container would start
   - front container would start

## Deploy

1. Deploy is automated with github actions. 
2. Project files used:
   - actions: .github/workflows/actions.yaml
   - compose file: deploy/docker-compose.yaml
   - variables in compose and env files are replaced with github secrets
3. Docker hub images:
   - front: sermalenk/skypro-front:lesson-38
   - back: Kibishicoder/Homework33:<tag>
4. To add admin during first launch:
   - connect to server and access project folder
   - `docker exec -it <api container_id> /bin/bash`
   - `./manage.py createsuperuser`


