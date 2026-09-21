# FastAPI Course API

A simple FastAPI application for managing posts and users with PostgreSQL and SQLAlchemy.

## Features

- Create, read, update, and delete posts
- Create users with bcrypt password hashing
- Retrieve a user by ID
- Interactive OpenAPI documentation
- Postman request collection under `postman/collections/FastAPI Course`

## Requirements

- Python 3.10 or newer
- PostgreSQL
- A PostgreSQL database named `fastapi`

## Setup

1. Create and activate a virtual environment:

   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

2. Install the dependencies:

   ```powershell
   pip install fastapi uvicorn sqlalchemy psycopg2-binary passlib[bcrypt] email-validator
   ```

3. Create the PostgreSQL database:

   ```sql
   CREATE DATABASE fastapi;
   ```

4. Ensure PostgreSQL is running and update the connection string in `app/database.py` if your local username, password, host, port, or database name differs.

   The current default is:

   ```text
   postgresql://postgres:22525994@localhost/fastapi
   ```

   Do not commit real database credentials. Use environment variables before deploying this application.

## Run the API

From the project root, run:

```powershell
uvicorn app.main:app --reload
```

The API is available at <http://127.0.0.1:8000>.

Interactive documentation:

- Swagger UI: <http://127.0.0.1:8000/docs>
- ReDoc: <http://127.0.0.1:8000/redoc>

## Endpoints

### General

| Method | Path | Description |
| --- | --- | --- |
| GET | `/` | Health-style welcome response |

### Posts

| Method | Path | Description |
| --- | --- | --- |
| GET | `/posts/` | List all posts |
| POST | `/posts/` | Create a post |
| GET | `/posts/{id}` | Get one post |
| PUT | `/posts/{id}` | Update a post |
| DELETE | `/posts/{id}` | Delete a post |

Create or update a post with JSON like:

```json
{
  "title": "My first post",
  "content": "Hello from FastAPI",
  "published": true
}
```

### Users

| Method | Path | Description |
| --- | --- | --- |
| POST | `/users/` | Create a user |
| GET | `/users/{id}` | Get a user without returning the password |

Create a user with JSON like:

```json
{
  "email": "user@example.com",
  "password": "secret-password"
}
```

## Project Structure

```text
app/
├── main.py              # FastAPI application and route registration
├── database.py          # SQLAlchemy engine and database session
├── models.py            # Database models
├── schemas.py           # Pydantic request and response schemas
├── utils.py             # Password hashing helpers
└── routers/
    ├── post.py          # Post endpoints
    └── user.py          # User endpoints
postman/                 # Postman collection, environment, and requests
```

Tables are created automatically when the application starts through SQLAlchemy metadata.
