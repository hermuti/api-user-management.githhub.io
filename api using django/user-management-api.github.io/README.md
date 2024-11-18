# user-management-api.github.io

A simple user management API built with Django and SQLite, including basic CRUD operations (Create, Read, Delete).

# User Management API

## Overview

The **User Management API** is a simple RESTful API built with **Django** and **SQLite**. It allows for basic user management operations, including the ability to create, list, and delete users. The API is designed to be a straightforward example of how to implement user management features in a web application.

### Features:

- **POST** `/users/`: Create a new user by sending a JSON payload containing a `name` and `email`.
- **GET** `/users/`: Retrieve a list of all users in the database.
- **DELETE** `/users/<id>/`: Delete a user by providing their unique `id`.

This API is useful for learning about Django, RESTful API design, and how to manage user data.

## Tools and Technologies

- **Django**: A high-level Python web framework that makes it easy to build web applications quickly. It handles routing, views, models, and database interactions.
- **SQLite**: A lightweight, file-based database that comes bundled with Django, perfect for development and small-scale applications.
- **Django REST Framework**: A toolkit for building Web APIs in Django. It simplifies creating RESTful APIs with serializers and views.
- **Python**: The programming language used to build this project.

## Installation

Follow the steps below to get this project up and running on your local machine.

### 1. Clone the Repository

Clone the repository to your local machine:

```bash
git clone https://github.com/username/user-management-api.git
cd user-management-api
```

### 2. Set Up a Virtual Environment

It's a good practice to use a virtual environment to manage dependencies. Run the following commands to set up a virtual environment and activate it:

For Windows:

```bash

Copy code
python -m venv venv
venv\Scripts\activate
For macOS/Linux:
```

```bash
Copy code
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

Install the required Python packages by running:

```bash
Copy code
pip install -r requirements.txt
```

### 4. Apply Migrations

Set up the SQLite database by applying the initial migrations:

```bash
Copy code
python manage.py migrate
This will create the necessary tables in the database, including the User model.
```

### 5. Run the Development Server

Start the Django development server:

```bash
Copy code
python manage.py runserver
The API will now be running at http://127.0.0.1:8000/.
```

**API Endpoints**
You can interact with the API using tools like Insomnia or Postman, or by writing your own HTTP requests.

### 1. POST /users/

Purpose: Create a new user.
Request Body (JSON):
json
Copy code
{
"name": "John Doe",
"email": "john.doe@example.com"
}
Response: A success message with the created user's information.

### 2. GET /users/

Purpose: Get a list of all users.
Response: A JSON array containing all users in the database.
json
Copy code
[
{
"id": 1,
"name": "John Doe",
"email": "john.doe@example.com"
},
{
"id": 2,
"name": "Jane Smith",
"email": "jane.smith@example.com"
}
]

### 3. DELETE /users/<id>/

Purpose: Delete a user by their unique id.
Example: To delete the user with id = 1, send a DELETE request to /users/1/.
Response: A success message confirming the user has been deleted.
How to Test the API
Once the server is running, you can test the API using Insomnia or Postman. Below are the steps for Insomnia:

Create a New Request: Select POST, GET, or DELETE depending on which endpoint you want to test.
Set the URL: Use http://127.0.0.1:8000/users/ (or http://localhost:8000/users/).
Add Request Body (for POST): Add a JSON payload with the user's name and email for the POST /users/ request.
Send the Request: Click Send to execute the request, and you should see the response from the server.
Usage Example
Creating a New User (POST /users/):
Request:

URL: http://127.0.0.1:8000/users/
Method: POST
Body (JSON):
json
Copy code
{
"name": "John Doe",
"email": "john.doe@example.com"
}
Response:

json
Copy code
{
"id": 1,
"name": "John Doe",
"email": "john.doe@example.com"
}
Listing All Users (GET /users/):
Request:

URL: http://127.0.0.1:8000/users/
Method: GET
Response:

json
Copy code
[
{
"id": 1,
"name": "John Doe",
"email": "john.doe@example.com"
}
]
Deleting a User (DELETE /users/<id>/):
Request:

URL: http://127.0.0.1:8000/users/1/
Method: DELETE
Response:

json
Copy code
{
"message": "User with ID 1 deleted successfully."
}
