# Contacts Management System

A modular Flask backend and web application for managing contact records with database persistence, ORM integration, and automated testing.

---

## Features

* **Modular Architecture**: Uses Flask Blueprints to decouple routes, database models, and app configurations.
* **Database ORM**: Powered by Flask-SQLAlchemy with support for SQLite and MySQL/MariaDB.
* **Environment Configuration**: Configured using `python-dotenv` for seamless development and production environment switching.
* **Full CRUD Operations**: Create, read, update, and delete contact records.
* **Automated Testing Suite**: Pre-configured testing framework using `pytest` and fixture setups.

---

## Project Structure

```text
.
├── app.py                     # Main Flask application factory and entry point
├── config.py                  # Configuration settings and environment variables
├── extensions.py              # Flask extension initializations (SQLAlchemy instance)
├── requirements.txt           # Project dependencies
├── database/
│   ├── __init__.py
│   └── init_db.py             # Script to populate/initialize database tables
├── models/
│   ├── __init__.py
│   └── contact.py             # SQLAlchemy Contact data model
├── routes/
│   ├── __init__.py
│   └── contact_routes.py      # Blueprint containing contact API/UI endpoints
├── static/
│   └── style.css              # Custom styling for frontend views
├── templates/
│   └── index.html             # Main dashboard UI template
└── tests/
    ├── conftest.py            # Pytest fixtures and app configuration for testing
    └── test_contacts.py       # Unit and integration tests for contact routes

```

---

## Installation & Setup

### 1. Prerequisites

Ensure you have Python 3.10+ installed on your machine.

### 2. Clone and Navigate to Project

```bash
cd 2508

```

### 3. Set Up Virtual Environment

```bash
# Create virtual environment
python -m venv venv

# Activate on Linux/macOS
source venv/bin/activate

# Activate on Windows
venv\Scripts\activate

```

### 4. Install Dependencies

```bash
pip install -r requirements.txt

```

### 5. Environment Configuration

Create a `.env` file in the root directory if customizing database credentials or secrets:

```env
FLASK_APP=app.py
FLASK_ENV=development
SECRET_KEY=your_secret_key_here
DATABASE_URL=sqlite:///instance/contacts.db

```

---

## Database Initialization

To set up the initial tables and sample database schema, run:

```bash
python -m database.init_db

```

---

## Running the Application

Start the Flask development server:

```bash
python app.py

```

The application will be accessible at: `[http://127.0.0.1:5000](http://127.0.0.1:5000)`

---

## Testing

Run the automated test suite using `pytest`:

```bash
pytest

```

To run tests with detailed output:

```bash
pytest -v

```

---

## Dependencies

* **Flask**: Web framework
* **Flask-SQLAlchemy**: ORM wrapper for database interactions
* **PyMySQL**: MySQL database connector driver
* **python-dotenv**: Loads environment variables from `.env`
* **pytest**: Test execution runner
