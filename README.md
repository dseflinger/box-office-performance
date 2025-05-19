# BoxOfficeApp
This is a project for analyzing box office performance, using two programs querying the same dataset in PostgreSQL:
 - Django
 - .NET 8.0 Console App (C#)
---
## Initial Setup Note

Before running either application, make sure to populate the database with sample data. The Django app includes a script (`load_data.py`) that inserts default data into the PostgreSQL database.

---
## Django App Setup
### Activate Virtual Environment
```
cd box_office_performance/django_app/django_app
python -m venv venv
venv/scripts/activate (or your path where activate file lives)
pip install -r requirements.txt
```
### PostgreSQL  Configuration
Make sure you have an unused database in PostgreSQL  with whatever credentials, name you like. You have two options to hook it up:
#### Option 1: Manually update settings.py
1. in settings.py manually set your database variables
2. replace name, user, password, host, and port with your own PostgreSQL  credentials
#### Option 2: Set up .env file for Environment Variables
1. At same level as manage.py create .env file with following config (replacing values with your own):
```
DB_NAME=your_db_name
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=your_host
DB_PORT=your_port
```
#### Create DB Tables and Load Sample Data
In your virtual environment:
```
python manage.py makemigrations
python manage.py migrate
python manage.py load_data.py
```
#### Running the app
In virtual environment
```
python manage.py runserver
```
The app will prompt you for a date and will give a revenue summary. There are other pages on the app including a movies, theaters, and sales page

---
## Console App Setup
### Requirements
- [.NET 8 SDK](https://dotnet.microsoft.com/en-us/download/dotnet/8.0)
- setup from PostgreSQL (same instance used by Django)
### Config
1. Copy settings from appsettings.sample.json to a new file appsettings.json
2. Replace appsettings.json with your actual PostgreSQL connection string
```
{
  "ConnectionStrings": {
    "DefaultConnection": "Host=yourHost;Port=yourPort;Database=your_db;Username=your_username;Password=your_password"
  }
}
```
#### Running the app
In terminal
```
cd console_app/boxoffice
dotnet run
```
The app will prompt you for a date and will give a revenue summary.

## Schema
See [schema explanation](schema/schema_explanation.md)
