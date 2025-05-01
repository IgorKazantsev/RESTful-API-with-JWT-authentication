# Raamatute RESTful API (FastAPI + JWT)

This is a practice project implementing a RESTful API for book management using JWT authentication and a role-based system (Admin / User).

## Roles and Permissions

- Admin:
  - Can add, update, and delete books.
  - Can view the activity logs.
- User:
  - Can view books.
  - Can add comments to books.

Note: The first registered user is assigned the "Admin" role. All subsequent users receive the "User" role.

## API Documentation

Swagger documentation is auto-generated and available at:

http://127.0.0.1:8000/docs

Swagger allows you to:
- View all endpoints and their request/response structures
- Test API calls
- Use JWT authentication via the "Authorize" button

## Running the Application

1. Create a `.env` file in the project root folder with the following content:

```
DATABASE_URL=...
SECRET_KEY=supersecretkey
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

2. Install the required dependencies:

```
pip install -r requirements.txt
```

3. Start the server:

```
uvicorn app.main:app --reload
```

## Project Structure

```

├── app/
│   ├── main.py
│   ├── models/
│   ├── schemas/
│   ├── routers/
│   ├── core/
│   └── ...
├── .env
├── requirements.txt
└── README.md
```

## Notes

- The API uses JWT-based authentication.
- User activity is logged.
- Only Admins can modify or delete book entries.
- All available endpoints are covered in the Swagger documentation.