LIBRARY API PROJECT - COMPLETE DJANGO PROJECT
=============================================

This is a complete Django REST API project for managing a library system.

PROJECT STRUCTURE
-----------------
library_project/
├── manage.py                    # Django management script
├── requirements.txt             # Python dependencies
├── README.txt                   # This file
├── library_project/             # Main project folder
│   ├── __init__.py
│   ├── settings.py             # Project settings
│   ├── urls.py                 # Main URL configuration
│   ├── wsgi.py
│   └── asgi.py
└── library/                     # Library app
    ├── __init__.py
    ├── models.py               # Database models
    ├── serializers.py          # REST serializers
    ├── views.py                # API views
    ├── urls.py                 # App URL configuration
    ├── admin.py                # Admin panel configuration
    ├── apps.py
    └── tests.py


QUICK START
-----------

1. INSTALL DEPENDENCIES
   pip install -r requirements.txt

2. RUN MIGRATIONS
   python manage.py makemigrations
   python manage.py migrate

3. CREATE ADMIN USER
   python manage.py createsuperuser

4. START SERVER
   python manage.py runserver

5. OPEN BROWSER
   Go to: http://localhost:8000/api/books/


AVAILABLE ENDPOINTS
-------------------

AUTHORS:
  GET    /api/authors/              - List all authors
  POST   /api/authors/              - Create new author
  GET    /api/authors/{id}/         - Get author details
  PUT    /api/authors/{id}/         - Update author
  DELETE /api/authors/{id}/         - Delete author

BOOKS:
  GET    /api/books/                - List all books
  POST   /api/books/                - Create new book
  GET    /api/books/{id}/           - Get book details
  PUT    /api/books/{id}/           - Update book
  DELETE /api/books/{id}/           - Delete book
  GET    /api/books/available/      - Get available books only
  POST   /api/books/{id}/borrow/    - Borrow a book
  POST   /api/books/{id}/return_book/ - Return a book

MEMBERS:
  GET    /api/members/              - List all members
  POST   /api/members/              - Register new member
  GET    /api/members/{id}/         - Get member details
  PUT    /api/members/{id}/         - Update member
  DELETE /api/members/{id}/         - Delete member
  GET    /api/members/{id}/borrowed_books/ - Get member's borrowed books

BORROW RECORDS:
  GET    /api/borrows/              - List all borrow records
  GET    /api/borrows/active/       - List active borrows


HOW TO USE
----------

1. ADD AN AUTHOR:
   POST to /api/authors/
   Body: {"name": "J.K. Rowling", "bio": "Author of Harry Potter"}

2. ADD A BOOK:
   POST to /api/books/
   Body: {
     "title": "Harry Potter",
     "author": 1,
     "isbn": "1234567890123",
     "total_copies": 5,
     "available_copies": 5
   }

3. REGISTER A MEMBER:
   POST to /api/members/
   Body: {
     "name": "John Doe",
     "email": "john@email.com",
     "phone": "1234567890"
   }

4. BORROW A BOOK:
   POST to /api/books/1/borrow/
   Body: {"member_id": 1}

5. RETURN A BOOK:
   POST to /api/books/1/return_book/
   Body: {"member_id": 1}


TESTING WITH CURL
-----------------

# List all books
curl http://localhost:8000/api/books/

# Add a book
curl -X POST http://localhost:8000/api/books/ \
  -H "Content-Type: application/json" \
  -d '{"title":"Test Book","author":1,"isbn":"1234567890123","total_copies":3,"available_copies":3}'

# Borrow a book
curl -X POST http://localhost:8000/api/books/1/borrow/ \
  -H "Content-Type: application/json" \
  -d '{"member_id":1}'


ADMIN PANEL
-----------
Access the admin panel at: http://localhost:8000/admin/
Use the superuser credentials you created


FEATURES
--------
- Complete CRUD operations for Books, Authors, and Members
- Borrow and return books functionality
- Automatic tracking of available copies
- Borrow history tracking
- REST API with browsable interface
- Admin panel for easy management


TROUBLESHOOTING
---------------

Problem: "No module named django"
Solution: Run "pip install -r requirements.txt"

Problem: "Table doesn't exist"
Solution: Run migrations:
  python manage.py makemigrations
  python manage.py migrate

Problem: "Port already in use"
Solution: Run on different port:
  python manage.py runserver 8080


NEXT STEPS
----------
- Add user authentication
- Add book categories
- Add search functionality
- Add book ratings
- Add late fees calculation
- Deploy to production server


SUPPORT
-------
This is a beginner-friendly project. All code is simple and well-commented.
Feel free to modify and extend as needed!
