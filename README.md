# Users API — Python, FastAPI & SQLite

A lightweight REST API built with **Python, FastAPI, and SQLite** to demonstrate user management, CRUD operations, request validation, and relational database integration.

## Overview

This project implements a simple user management API with endpoints for creating, retrieving, updating, and deleting user records.

It was developed as a practical exercise in Python backend development, focusing on RESTful endpoints, SQL operations, and structured request and response handling.

## Features

- Create new users
- Retrieve all registered users
- Find a user by email
- Update user information
- Delete user records
- Validate request data using Pydantic
- Enforce unique email addresses
- Return appropriate HTTP errors for missing users and duplicate emails
- Interactive API documentation provided by FastAPI

## Tech Stack

- Python
- FastAPI
- SQLite
- Pydantic
- Uvicorn
- SQL

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Welcome message and user count |
| GET | `/users` | Retrieve all users |
| POST | `/users` | Create a user |
| GET | `/users/{email}` | Retrieve a user by email |
| PUT | `/users/{email}` | Update a user |
| DELETE | `/users/{email}` | Delete a user |

## Example Requests

### Create a User

**POST `/users`**

```json
{
  "name": "Jane Doe",
  "email": "jane@example.com"
}
```

### Retrieve Users

```bash
curl http://127.0.0.1:8000/users
```

### Find a User

```bash
curl http://127.0.0.1:8000/users/jane@example.com
```

### Delete a User

```bash
curl -X DELETE http://127.0.0.1:8000/users/jane@example.com
```

## Database

The application uses SQLite for local data persistence.

The `users` table contains:

| Field | Type | Constraint |
|-------|------|------------|
| id | INTEGER | Primary key |
| name | TEXT | Required |
| email | TEXT | Required, unique |

SQL queries use parameterized statements for user-provided values.

## Getting Started

### Prerequisites

- Python 3
- pip

### Installation

```bash
git clone https://github.com/jlcambraia/users-fastapi-sqlite.git
cd users-fastapi-sqlite
python -m venv venv
```

Activate the environment on Linux/macOS:

```bash
source venv/bin/activate
```

Or on Windows:

```powershell
venv\Scripts\activate
```

Install dependencies and initialize the database:

```bash
pip install -r requirements.txt
python database.py
```

Start the API:

```bash
uvicorn main:app --reload
```

## API Documentation

FastAPI automatically provides interactive documentation:

- Swagger UI: http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc

## Project Structure

```text
users-fastapi-sqlite/
├── main.py
├── database.py
├── requirements.txt
└── README.md
```

- `main.py` — API routes, Pydantic model, and database operations
- `database.py` — SQLite database initialization
- `requirements.txt` — Python dependencies

## Project Scope

This is an educational backend project designed for local development. It is not intended to be a production-ready identity management service.

## Potential Improvements

- Automated API tests
- More comprehensive email validation
- Authentication and authorization
- Environment-based configuration
- Database migrations
- Improved error handling
- Separation of routes and database services

## Author

**João Luiz Cambraia**

[GitHub](https://github.com/jlcambraia) · [LinkedIn](https://www.linkedin.com/in/joaoluizcambraia/)
