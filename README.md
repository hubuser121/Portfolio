Portfolio Project - Django Web Application
Overview
This project is my personal portfolio website, developed using Django, a powerful and flexible Python web framework. The portfolio showcases my software development projects, certificates, and skills with a clean, professional, and responsive design.

What This Project Does
Presents a Home page introducing myself and my objectives.

Displays a Projects page where all completed coding projects are showcased with descriptions and live or GitHub links.

Includes a Certificates page enumerating my professional and educational achievements.

Provides an admin interface for easy management of portfolio content without modifying code.

Utilizes Django’s powerful templating and routing system to render dynamic content.

Collects and serves static files (CSS, JavaScript, images) properly for styling and usability.

Technologies and Tools Used
Python 3.13: Programming language backend.

Django 5.2.8: Web framework used to build and organize the web application.

SQLite: Default database for storing project and certificate data.

WhiteNoise: Middleware used to serve static files efficiently in production.

Git & GitHub: Version control and remote repository hosting.

Virtual Environment (venv): Isolates project dependencies.

HTML, CSS, Bootstrap: Frontend technologies for responsive design.

Gunicorn (optional for deployment): Application server for running Django in production environments.

Key Learnings and Accomplishments
Successfully structured a Django project with multiple apps and template inheritance.

Implemented responsive layouts and UI elements for professional look and feel.

Configured Django settings for production, including ALLOWED_HOSTS, static files collection, and CSRF protection.

Handled version control with Git and remote repository management on GitHub.

Performed deployment preparations such as running migrations, creating superusers, and managing static assets.

Gained experience resolving common deployment errors like DisallowedHost and CSRF verification failures.

Improved understanding of deployment platforms by experimenting with hosting options and setting up environment variables.

How to Run This Project Locally
Clone the project:

text
git clone https://github.com/hubuser121/Portfolio.git
Navigate to the project folder and create a virtual environment:

text
python -m venv venv
venv\Scripts\activate  # (Windows)
source venv/bin/activate  # (Linux/Mac)
Install dependencies:

text
pip install -r requirements.txt
Run database migrations:

text
python manage.py migrate
Collect static files:

text
python manage.py collectstatic
Create a superuser account to access Django admin:

text
python manage.py createsuperuser
Start the development server:

text
python manage.py runserver
Open your browser at http://127.0.0.1:8000 and explore your portfolio.

Access the admin panel at http://127.0.0.1:8000/admin to add or modify content.

Deployment Notes
Configure ALLOWED_HOSTS in settings.py to match your deployment domain.

Use WhiteNoise middleware to serve static files in production.

Make sure to run collectstatic before deploying.

Secure your SECRET_KEY and database credentials with environment variables.

Keep DEBUG=False in production for security.

Future Enhancements
Add user authentication and contact forms.

Integrate AI assistant features or chatbot.

Improve UI with animations and enhanced interactivity.

Automate deployment with GitHub Actions or CI/CD pipelines.
