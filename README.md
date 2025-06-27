  "Book Review Sercvice" 
 
 project using Python, Django REST Framework + MySQL + POSTMAN


📚 Book Review API
A simple RESTful API that allows users to:

List all books

Add a new book

View reviews for a specific book

Add a review to a book


🚀 Features
✅ RESTful API with CRUD operations

✅ MySQL database with Django ORM

✅ Postman documentation

✅ Error handling for cache and database

🧑‍💻 Tech Stack
Python 3.x
Django 4.x
Django REST Framework
MySQL
POSTMAN

⚙️ Setup Instructions
1. Clone the Repository
git clone https://github.com/your-username/book-review-api.git
cd book-review-api

2. Create Virtual Environment
python -m venv venv
venv\Scripts\activate    

4. Install Dependencies
pip install -r requirements.txt

5. Configure Database
In bookreview/settings.py, update your MySQL settings:

DATABASES = {
  'default': {
    'ENGINE': 'django.db.backends.mysql',
    'NAME': 'BookDB',
    'USER': '****',
    'PASSWORD': 'your_db_password',
    'HOST': 'localhost',
    'PORT': '3306',
  }
}


5. Apply Migrations
python manage.py makemigrations
python manage.py migrate
python manage.py runserver

📖 API Endpoints
Method	Endpoint	Description
GET	/books/	Get all books (cached)
POST	/books/	Add a new book
GET	/books/{id}/reviews/	Get reviews of a book
POST	/books/{id}/reviews/	Add review for a book

📚 API Documentation
Visit POSTMAN UI:
http://127.0.0.1:8000/POSTMAN/
