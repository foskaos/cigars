# Cigar Collection Application Backend

This repository contains the backend API for a cigar collection application built with FastAPI and SQLAlchemy. The API provides endpoints for user authentication, user management, and managing cigar collections.

## Table of Contents

- [Cigar Collection Application Backend](#cigar-collection-application-backend)
  - [Table of Contents](#table-of-contents)
  - [Overview](#overview)
  - [Features](#features)
  - [Tech Stack](#tech-stack)
  - [Project Structure](#project-structure)
  - [Setup and Installation](#setup-and-installation)
  - [Running the Application](#running-the-application)
  - [API Documentation](#api-documentation)
    - [Authentication](#authentication)
    - [User Management](#user-management)
    - [Cigar Management](#cigar-management)
  - [Weaknesses and Improvements](#weaknesses-and-improvements)
  - [Contributing](#contributing)
  - [License](#license)

## Overview

The backend API for the cigar collection application is built using FastAPI and SQLAlchemy, providing a robust and scalable solution for managing users and their cigar collections. The API uses JWT for authentication and supports CRUD operations for both users and cigars.

## Features

- User registration and authentication
- JWT-based authentication
- CRUD operations for cigars
- Eager loading of relationships to avoid lazy loading issues
- Asynchronous database operations

## Tech Stack

- **Language:** Python
- **Framework:** FastAPI
- **Database:** PostgreSQL
- **ORM:** SQLAlchemy
- **Authentication:** JWT (JSON Web Tokens)
- **Containerization:** Docker, Docker Compose

## Project Structure

```
cigar-app/
│
├── app/
│   ├── __init__.py
│   ├── auth.py
│   ├── crud.py
│   ├── database.py
│   ├── dependencies.py
│   ├── main.py
│   ├── models.py
│   ├── routers/
│   │   ├── __init__.py
│   │   ├── auth.py
│   │   ├── cigars.py
│   │   ├── users.py
│   ├── schemas.py
│   ├── security.py
│
├── alembic/
│   ├── env.py
│   ├── script.py.mako
│   └── versions/
│       └── (migration files)
│
├── alembic.ini
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```

## Setup and Installation

### Prerequisites

- Docker and Docker Compose installed on your machine

### Installation Steps

1. **Clone the repository:**

```sh
git clone https://github.com/yourusername/cigar-app.git
cd cigar-app
```

2. **Create a `.env` file in the root directory and add the following environment variables:**

```sh
DATABASE_URL=postgresql+asyncpg://user:password@db/cigar_db
SECRET_KEY=your_secret_key
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

3. **Build and run the Docker containers:**

```sh
docker-compose up --build
```

4. **Run database migrations:**

```sh
docker-compose exec app alembic upgrade head
```

The application should now be running on `http://localhost:8000`.

## Running the Application

The application is containerized using Docker. To run the application:

1. **Start the Docker containers:**

```sh
docker-compose up
```

2. **Access the API documentation:**

Open your browser and navigate to `http://localhost:8000/docs` to view the interactive API documentation.

## API Documentation

### Authentication

#### POST /token

Authenticate a user and return a JWT token.

**Request:**

- Content-Type: `application/x-www-form-urlencoded`
- Body:

```plaintext
grant_type=&username=<username>&password=<password>&scope=&client_id=&client_secret=
```

**Response:**

- 200 OK
- Body:

```json
{
  "access_token": "<token>",
  "token_type": "bearer"
}
```

### User Management

#### POST /users/

Create a new user.

**Request:**

- Content-Type: `application/json`
- Body:

```json
{
  "username": "testuser",
  "email": "testuser@example.com",
  "password": "testpassword"
}
```

**Response:**

- 201 Created
- Body:

```json
{
  "id": 1,
  "username": "testuser",
  "email": "testuser@example.com",
  "cigars": []
}
```

#### GET /users/me/

Retrieve the current authenticated user's details.

**Request:**

- Headers:
  - Authorization: `Bearer <token>`

**Response:**

- 200 OK
- Body:

```json
{
  "id": 1,
  "username": "testuser",
  "email": "testuser@example.com",
  "cigars": [
    {
      "id": 1,
      "name": "Cigar Example",
      "brand": "Brand Example",
      "origin": "Cuba",
      "flavor_notes": "Rich and full-bodied",
      "rating": 5,
      "owner_id": 1
    }
  ]
}
```

### Cigar Management

#### GET /cigars/

Retrieve a list of cigars.

**Request:**

- Query Parameters:
  - `skip` (integer, optional): Number of records to skip (default: 0)
  - `limit` (integer, optional): Maximum number of records to return (default: 10)

**Response:**

- 200 OK
- Body:

```json
[
  {
    "id": 1,
    "name": "Cigar Example",
    "brand": "Brand Example",
    "origin": "Cuba",
    "flavor_notes": "Rich and full-bodied",
    "rating": 5,
    "owner_id": 1
  }
]
```

#### POST /cigars/

Add a new cigar to the authenticated user's collection.

**Request:**

- Headers:
  - Authorization: `Bearer <token>`
- Content-Type: `application/json`
- Body:

```json
{
  "name": "New Cigar",
  "brand": "New Brand",
  "origin": "Dominican Republic",
  "flavor_notes": "Smooth and creamy",
  "rating": 4
}
```

**Response:**

- 201 Created
- Body:

```json
{
  "id": 2,
  "name": "New Cigar",
  "brand": "New Brand",
  "origin": "Dominican Republic",
  "flavor_notes": "Smooth and creamy",
  "rating": 4,
  "owner_id": 1
}
```

## Weaknesses and Improvements

### Weaknesses

1. **Security:** The current implementation uses a hardcoded secret key in the `.env` file, which is not secure for production environments.
2. **User Management:** There is no email verification for new users, which could lead to fake accounts being created.
3. **Error Handling:** The error handling could be improved to provide more informative error messages.
4. **Scalability:** The current setup is suitable for a small scale application but may require optimizations for larger scale deployments.

### Improvements

1. **Environment Configuration:** Use a more secure method to manage environment variables and secrets, such as AWS Secrets Manager or Azure Key Vault.
2. **Email Verification:** Implement email verification for new users to enhance security.
3. **Enhanced Error Handling:** Improve error handling to provide more detailed error messages and logging.
4. **Testing:** Add comprehensive unit and integration tests to ensure the reliability of the application.
5. **Scalability Enhancements:** Optimize database queries and consider implementing caching mechanisms to improve performance for larger datasets.

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes.

1. Fork the repository
2. Create a new branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Create a new pull request

## License

This project is licensed under the MIT License.

---

This comprehensive README file should provide a clear and complete guide for the front-end developer to understand and use the backend API. If there are any further questions or additional details required, please feel free to ask.