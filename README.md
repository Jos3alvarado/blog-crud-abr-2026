# CRUD Application

## Project Overview
This project is a Django-based CRUD (Create, Read, Update, Delete) application. It is designed to manage articles and user authentication, providing a simple yet robust framework for learning and implementing CRUD operations in a web application.

---

## Features
- **User Authentication**: Includes login and signup functionality.
- **Article Management**: Users can create, view, update, and delete articles.
- **Responsive Design**: Styled with CSS for a clean and user-friendly interface.

---

## Project Structure
```
CRUD_abr2026/
├── db.sqlite3
├── manage.py
├── requirements.txt
├── base_project/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── newspaper/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
│   └── migrations/
│       ├── __init__.py
│       └── 0001_initial.py
├── signup/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
│   └── migrations/
│       ├── __init__.py
├── static/
│   └── css/
│       └── style.css
└── templates/
    ├── _base.html
    ├── article-create.html
    ├── article-delete.html
    ├── article-detail.html
    ├── article-list.html
    ├── article-update.html
    └── registration/
        ├── login.html
        └── signup.html
```

---

## Installation

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd CRUD_abr2026
   ```

2. **Set Up Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply Migrations**:
   ```bash
   python manage.py migrate
   ```

5. **Run the Development Server**:
   ```bash
   python manage.py runserver
   ```

---

## Usage

1. Open your browser and navigate to `http://127.0.0.1:8000/`.
2. Sign up or log in to access the article management features.
3. Create, view, update, or delete articles as needed.

---

## File Descriptions

### `base_project/`
Contains the core Django project files, including settings and URL configurations.

### `newspaper/`
Handles the article management functionality, including models, views, and templates.

### `signup/`
Manages user authentication, including signup and login features.

### `static/`
Contains static files such as CSS for styling.

### `templates/`
Houses HTML templates for rendering the frontend.

---

## Contributing

1. Fork the repository.
2. Create a new branch for your feature:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add feature description"
   ```
4. Push to the branch:
   ```bash
   git push origin feature-name
   ```
5. Open a pull request.

---

## License
This project is licensed under the MIT License. See the LICENSE file for details.

---

## Contact
For questions or feedback, please contact:
- **Name**: Jose A.
- **Email**: [your-email@example.com]

---

## Screenshots
Include screenshots of the application here to showcase its functionality and design.

---

Thank you for using this CRUD application!