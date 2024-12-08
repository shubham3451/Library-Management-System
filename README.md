Django Library Management System

This project implements a Library Management System using Django. It allows the management of books and members, supporting CRUD operations and features like search, pagination, and token-based authentication.
Table of Contents

    Prerequisites
    How to Run the Project
    Design Choices
    Assumptions and Limitations

Prerequisites

Before running the project, ensure that you have the following installed:

    Python (3.7 or higher)
    Django (4.0 or higher)
    Django Rest Framework (DRF) for building APIs
    SQLite (default database for Django) or any other compatible database (if you change the settings)

If Django and DRF are not installed, you can install them using pip:

pip install django
pip install djangorestframework

How to Run the Project

Follow these steps to set up and run the project on your local machine:
1. Clone the repository

git clone https://github.com/shubham3451/Library-Management-System.git
cd library-management-system

2. Set up a virtual environment (optional but recommended)

python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3. Install dependencies

pip install django djangorestframework

4. Apply migrations

To set up the database and create the required tables, run:

python manage.py makemigrations
python manage.py migrate

5. Create a superuser (optional, for accessing the admin interface)

You can create a superuser to access the Django admin interface:

python manage.py createsuperuser

6. Run the development server

Now, run the development server to start the project:

python manage.py runserver

The API will be available at http://127.0.0.1:8000/api/, and the Django admin interface will be accessible at http://127.0.0.1:8000/admin/.
7. Access the API

    GET /api/books/: List all books.
    POST /api/books/: Add a new book.
    GET /api/books/{id}/: Get details of a specific book.
    PUT /api/books/{id}/: Update details of a book.
    DELETE /api/books/{id}/: Delete a book.

Search Books by Title or Author:

    GET /api/books/search/?query={search_term}: Search books by title or author.

    GET /api/members/: List all members.

    POST /api/members/: Add a new member.

    GET /api/members/{id}/: Get details of a specific member.

    PUT /api/members/{id}/: Update details of a member.

    DELETE /api/members/{id}/: Delete a member.

Design Choices
1. Django Framework

Django was chosen because of its robust features for building web applications quickly, including:

    Admin Interface: The Django admin panel provides an easy way to manage the database models (books and members) without requiring custom frontend development.
    ORM: Django's Object-Relational Mapping (ORM) allows seamless interaction with the database without having to write raw SQL queries, making database operations more convenient.
    Security: Django provides built-in security features like SQL injection protection, cross-site request forgery (CSRF) protection, and secure authentication mechanisms.

2. Django Rest Framework (DRF)

For building the API, Django Rest Framework was used due to its ease of use and flexibility. Some of the key benefits include:

    Serializers: DRF provides automatic conversion of Python objects (models) to JSON, making it easy to handle API responses.
    Views: DRF’s APIView class allows us to easily handle CRUD operations and customize how data is handled.
    Pagination: Built-in pagination support allows us to limit the number of results returned in each API request (e.g., 5 books per page).
    Token-based Authentication: We implemented a simple token-based authentication system to secure the API.

3. Token Authentication

We used Django's default token-based authentication, which requires users to authenticate via a token in the header of each API request. This prevents unauthorized access to sensitive operations.
4. Pagination

We implemented pagination using Django's built-in PageNumberPagination. This helps with large datasets by returning a fixed number of results per page and providing links to the next and previous pages.
Assumptions and Limitations
Assumptions:

    Simple Authentication: The system uses basic token-based authentication (without third-party libraries), and it assumes the user has already obtained the token and includes it in the request headers.
    Basic Search: The search functionality is based on case-insensitive matches of the title or author of the books. This could be expanded with more advanced search techniques (e.g., fuzzy search or multi-parameter searches).
    No External Services: The system does not integrate with external APIs or services. Everything is handled within the Django application.
    Single Database: This project assumes the use of the default SQLite database (which comes with Django). You can switch to other databases (e.g., PostgreSQL) by modifying the database settings in settings.py.

Limitations:

    No User Management: While token authentication is implemented, the user management (e.g., registration, password reset) is not part of this project. Only basic user creation is supported via Django’s default authentication system.
    No Advanced Search Features: The search functionality is limited to searching for books by title or author. More complex searches (e.g., by genre, publication year) are not supported out of the box.
    Pagination: Pagination is limited to 5 books per page by default. This can be customized but is set to a small value for demonstration purposes.
    No Frontend: The project focuses solely on the backend API. There is no frontend or UI built for end-users. The API could be consumed by any frontend (e.g., React or Angular).

Future Enhancements

    User Management: Implement user registration, login, and password reset functionalities.
    Advanced Search: Extend the search to support searching by multiple fields (e.g., genre, year, ISBN).
    Frontend Interface: Create a simple frontend UI to interact with the backend.
    File Uploads: Add support for uploading book cover images.
    Enhanced
