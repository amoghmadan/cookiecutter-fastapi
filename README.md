# Cookiecutter FastAPI

Use this template to create a FastAPI Python project.

## How to use?

- Set-up base.
  ```bash
  cookiecutter https://github.com/amoghmadan/cookiecutter-fastapi.git
  ```
- Follow the prompts to customize your project.
  ```
  [1/4] project_name (app): play
  [2/4] project_description (Example application): Play with cookie cutter.
  [3/4] author_name (Your Name): Your Name
  [4/4] author_email (your@email.com): your@email.com
  ```

## Set-up?

- Initialize Git, it is very important for the project to work.
  ```bash
  git init -b main
  ```
- Create a virtual environment.
  ```bash
  python3.13 -m venv .venv
  ```
- Activate the virtual environment.
    ```bash
    source .venv/bin/activate
    ```
- Install the dependencies (you can select database from mysql, postgres, sqlite).
  ```bash
  pip install -e '.[automation,test]'
  ```

## How to run?

- Run the server.
  ```bash
  {{project_name}} runserver
  ```
- Load JSON data (fixtures) into your models.
  ```bash
  {{project_name}} loaddata <file>.json
  ```
- Run the python shell (with application context).
  ```bash
  {{project_name}} shell
  ```
