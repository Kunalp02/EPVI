# E-commerce APIs

This project provides a e-commerce API built with Django, Django REST framework, PostgreSQL, and Redis for caching. It includes user authentication, product management, an order system, a shopping cart, and real-time notifications using WebSockets.

## Prerequisites

Ensure you have the following installed:

- Python 3.x
- PostgreSQL
- Redis
- Docker (optional for running Redis and PostgreSQL via Docker)
- pip (Python package installer)

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-repository/ecommerce-api.git
cd ecommerce-api
```

### 2. Create and Activate a Virtual Environment
Create a virtual environment to isolate project dependencies.
```
bash

python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```
### 3. Install Dependencies
Install the required Python dependencies listed in the requirements.txt file.
```
bash
pip install -r requirements.txt
```
### 4. Configure PostgreSQL Database
Ensure PostgreSQL is running on your system.
Create a PostgreSQL database and user:
```
sql
CREATE DATABASE your_db_name;
CREATE USER your_db_user WITH PASSWORD 'your_password';
ALTER ROLE your_db_user SET client_encoding TO 'utf8';
ALTER ROLE your_db_user SET default_transaction_isolation TO 'read committed';
ALTER ROLE your_db_user SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE your_db_name TO your_db_user;
```
Update the DATABASES section in settings.py with your database credentials:
```
python

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_db_name',
        'USER': 'your_db_user',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```
### 5. Configure Redis for Caching
Ensure Redis is running on your system.
In settings.py, configure Redis as the cache backend:
python
```
CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://127.0.0.1:6379/1',
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        }
    }
}
```

### 6. Run Migrations
Apply migrations to set up the database schema.
```
python manage.py makemigrations
python manage.py migrate
```


```
bash

python manage.py migrate
7. Create a Superuser
Create a superuser to manage the admin interface.
```
```
bash

python manage.py createsuperuser
8. Run the Development Server
Start the Django development server.
```
```
bash

python manage.py runserver
You can now access the API at http://127.0.0.1:8000/api/.
and docs at http://127.0.0.1:8000/docs/
```
