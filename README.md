1. Clone project in your system
2. Create virtual environment using 'python -m venv venv'
3. Activate virtual environment using 'venv\Scripts\activate'
4. Install all the required packages using 'pip install -r requirements.txt'
5. Create .env file in project directory and add required variables to it
6. Migrate tables to your database using following commands:
   * python manage.py makemigrations
   * python manage.py migrate
7. Run server using 'python manage.py runserver'
8. Call api end point(http://127.0.0.1:8000/employee/add/) to add data to database