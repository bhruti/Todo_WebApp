# Django To-Do App

A To-Do application built using Django with SQLite as the database. Users can register, log in, add tasks, mark tasks as complete, and delete tasks.

## Features
- User registration and authentication
- Add tasks to the to-do list
- View all tasks in the same window
- Update task status to "Complete"
- Delete tasks

## Technologies Used
- Django
- SQLite (default Django database)
- HTML, CSS (for frontend)

## Installation and Setup

### Prerequisites
Make sure you have Python installed on your system.

### Steps to Run the Project

1. **Clone the repository:**
   ```sh
   git clone https://github.com/bhruti/Todo_WebApp
   ```

2. **Create and activate a virtual environment (Optional but recommended):**
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies:**
   ```sh
   cd todopro
   pip install -r requirements.txt
   ```

4. **Apply migrations:**
   ```sh
   python manage.py migrate
   ```

5. **Create a superuser (**optional**, for admin access):**
   ```sh
   python manage.py createsuperuser
   ```
   Follow the prompts to create an admin user.

6. **Run the development server:**
   ```sh
   python manage.py runserver
   ```
   The application will be accessible at `http://127.0.0.1:8000/`

## Usage
1. Register a new user.
2. Log in using your credentials.
3. Add tasks using the provided form.
4. View your tasks in the list.
5. Mark tasks as complete or delete them as needed.

### Demo Video
https://youtu.be/aat3BBxjtqM

