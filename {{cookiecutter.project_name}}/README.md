# {{cookiecutter.project_name}}

{{cookiecutter.project_name}} API

## Setup Virtual Environment

- How to set up?
  ```bash
  python3.13 -m venv .venv
  ```

## How to set up?

- How to install dependencies?
  ```bash
  pip install -e '.[automation,test]'
  ```

## How to run a development server?

- Run the development server.
  ```bash
  {{cookiecutter.project_name}} runserver
  ```

## Migrations

- Make migration files
  ```bash
  alembic revision --autogenerate -m "Your message here"
  ```
- Migrate
  ```bash
  alembic upgrade head
  ```
  
## How to load fixtures?

- Use the following command to load fixtures from a JSON file.
  ```bash
  {{cookiecutter.project_name}} loaddata <file>.json
  ```
  
## How to run Python REPL?

- Use the following command to run the Python Shell with context.
  ```bash
  {{cookiecutter.project_name}} shell
  ```

## How to build an image for deployment?

- Use the following command to build deployable image.
  ```bash
  docker build -t {{cookiecutter.project_name}}:$(python -c "from {{cookiecutter.project_name}} import __version__;print(__version__)") .
  ```
