To set up a Django environment properly, follow these steps:

✅ Step-by-Step Django Environment Setup
1️⃣ Install Python
First, check if Python is installed:


python --version
If Python is not installed, download and install it from:
🔗 https://www.python.org/downloads/

2️⃣ Create a Virtual Environment (Recommended)
To keep dependencies organized, create a virtual environment:


python -m venv venv
Now, activate the virtual environment:

🔹 Windows (Command Prompt or PowerShell):


venv\Scripts\activate
🔹 Mac/Linux:


source venv/bin/activate
After activation, your terminal will show (venv) before the command line.

3️⃣ Install Django & Required Packages
Now, install Django and Django REST Framework:


pip install django djangorestframework
4️⃣ Create a Django Project
Run:


django-admin startproject gas_utility
cd gas_utility
5️⃣ Create Django Apps
Create the required Django apps inside the project:


python manage.py startapp service_requests
python manage.py startapp users
6️⃣ Add Apps to settings.py
Open gas_utility/settings.py and add these apps inside INSTALLED_APPS:


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',  # Django REST Framework
    'service_requests',  # Service Request App
    'users',  # Authentication App
]
7️⃣ Apply Migrations
Run:


python manage.py makemigrations
python manage.py migrate
8️⃣ Create a Superuser
To access the Django Admin panel:


python manage.py createsuperuser
Enter username, email, and password.

9️⃣ Run the Server
Start the Django development server:


python manage.py runserver
Now, open http://127.0.0.1:8000/admin/ in your browser and log in with the superuser credentials.
