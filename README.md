# 📝 Django To-Do Application with CI/CD

A backend-focused To-Do Application built using **Python and Django**. The application provides APIs to create, read, update, and delete tasks.

The project also includes a **CI/CD pipeline using GitHub Actions** to automate testing and deployment to a production server.

---

## 🚀 Features

- Create To-Do tasks
- Retrieve all tasks
- Retrieve a single task
- Update existing tasks
- Delete tasks
- Mark tasks as completed
- RESTful API architecture
- Django ORM for database operations
- Environment-based configuration
- Automated testing
- Automated CI/CD pipeline
- Automated deployment using SSH
- Gunicorn application server
- Nginx reverse proxy
- Production deployment on Linux server

---

## 🛠️ Tech Stack

### Backend

- Python
- Django
- Django REST Framework
- Django ORM

### Database

- SQLite for development
- PostgreSQL / MySQL for production

### DevOps

- Git
- GitHub
- GitHub Actions
- Linux
- Gunicorn
- Nginx
- SSH
- Azure VM / Cloud Server

---

## 📁 Project Structure

```text
django-todo-application/
│
├── todo_project/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
│
├── todo/
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── urls.py
│   ├── views.py
│   └── tests.py
│
├── .github/
│   └── workflows/
│       └── ci-cd.yml
│
├── manage.py
├── requirements.txt
├── .gitignore
└── README.md
