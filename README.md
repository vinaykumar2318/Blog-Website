# Django Blog Website

Welcome to the Django Blog Website! This project is a simple blogging platform built using Django, featuring user authentication and styled forms using Django Crispy Forms.

## Features

- User Registration and Authentication
- Create, Read, Update, and Delete Blog Posts
- Responsive and Clean User Interface
- Styled Forms using Django Crispy Forms
- Secure Password Handling

## Technologies Used

- **Backend**: Django
- **Frontend**: HTML, CSS, Bootstrap
- **Forms**: Django Crispy Forms
- **Database**: SQLite (default, can be changed)
- **Authentication**: Django's built-in authentication system

## Installation

### Prerequisites

Make sure you have the following installed on your machine:

- Python 3.6+
- pip (Python package installer)
- Virtualenv (optional, but recommended)

### Steps

1. **Clone the repository**

    ```bash
    git clone https://github.com/yourusername/django-blog.git
    cd django-blog
    ```

2. **Create a virtual environment**

    ```bash
    python -m venv venv
    ```

3. **Activate the virtual environment**

    - On Windows:

        ```bash
        venv\Scripts\activate
        ```

    - On macOS/Linux:

        ```bash
        source venv/bin/activate
        ```

4. **Install the required packages**

    ```bash
    pip install -r requirements.txt
    ```

5. **Apply migrations**

    ```bash
    python manage.py migrate
    ```

6. **Create a superuser**

    ```bash
    python manage.py createsuperuser
    ```

    Follow the prompts to create a superuser account.

7. **Run the development server**

    ```bash
    python manage.py runserver
    ```

8. Open your web browser and go to `http://127.0.0.1:8000/` to see the website in action.

## Configuration

### Django Crispy Forms

Crispy Forms is used to style forms in this project. Make sure to add `'crispy_forms'` to your `INSTALLED_APPS` in `settings.py`.
