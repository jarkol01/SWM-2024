# App for SWM hackathon

# Prerequisites

## Native way with virtualenv
- [Python3.10](https://www.python.org/downloads/)
- [Virtualenv](https://virtualenv.pypa.io/en/latest/)

## Docker way
- [Docker](https://docs.docker.com/engine/install/)  
- [Docker Compose](https://docs.docker.com/compose/install/)

## Local Development

## Native way with virtualenv

First create postgresql database:

```sql
create user SWM2024 with createdb;
alter user SWM2024 password 'SWM2024';
create database SWM2024 owner SWM2024;
```
Now you can setup virtualenv and django:
```bash
virtualenv venv
source venv/bin/activate
pip install pip-tools
make bootstrap
```

## Docker way

Start the dev server for local development:
```bash
docker-compose up
```

Run a command inside the docker container:

```bash
docker-compose run --rm web [command]
```


## Pre-commit hooks

To install pre-commit hooks run:

```bash
pre-commit install
pre-commit install -t commit-msg
```

Currently, pre_ticket hook works only when commit message is passed as a `-m` parameter to a git commit command.

## Login to admin panel

To log in the admin panel, you can use the following credentials:

Username: admin
Password: admin321!
