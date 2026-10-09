# Flask Library API

A Python library API exercise using Flask, Flask-RESTful, and SQLAlchemy. The application separates controllers, services, repositories, and models.

## Application location

The application is in `flask_library/`. Run commands from that directory, not the repository root. The PDF in the root contains the assignment guide.

## Run locally

Requires Python 3 and pip.

```sh
cd flask_library
```

```sh
python -m venv .venv
# Windows PowerShell:
.\.venv\Scripts\Activate.ps1
# macOS/Linux: source .venv/bin/activate
python -m pip install -r requirements.txt
python app.py
```

The application uses SQLite at `sqlite:///library.db`. Tables are created before requests are handled.

## API routes

- `/api/library`: library collection resource.
- `/api/library/<isbn>`: individual book resource.

The server normally runs at `http://127.0.0.1:5000`. Inspect `flask_library/controller/` for supported methods and request fields.

## Structure

- `app.py`: Flask application, database configuration, and route registration.
- `controller/`: HTTP resources.
- `service/`: service logic.
- `repositories/`: data-access layer.
- `models/`: SQLAlchemy models.
- `requirements.txt`: dependencies.

This is coursework. The startup entry point enables Flask debug mode for local development.

## Attribution

This repository is a fork of [programming-languages-38562/python-flask-api](https://github.com/programming-languages-38562/python-flask-api).
