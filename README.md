# Python FastAPI REST Starter

Kick-starter to your REST application.

## How to set up project for development?

- Create a virtual environment: -
  ```bash
  python -m venv venv
  ```
- Activate: -
    - Windows: `venv\Scripts\activate`
    - Unix-like: `. venv\bin\activate`
- Install dependencies: -
  ```bash
  pip install . -e '.[automation,sqlite,test]'
  ```
- Run: -
  ```bash
  uvicorn app.asgi:application --reload
  ```

## How to set up project for deployment?

- Create a virtual environment: -
  ```bash
  python -m venv venv
  ```
- Activate: -
    - Windows: `venv\Scripts\activate`
    - Unix-like: `. venv\bin\activate`
- Install dependencies: -
  ```bash
  pip install -e '.[sqlite,deployment]'
  ```
- Run: -
  ```bash
  gunicorn app:asgi:application -b 0.0.0.0:8000 -w 4 -k uvicorn.workers.UvicornWorker --log-level INFO
  ```
