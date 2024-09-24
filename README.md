Flask Notes App
This is a basic web application built using Flask, allowing users to sign up, log in, and create notes. The application supports user authentication using flask-login and handles CRUD operations for notes using SQLAlchemy ORM.

Features
User authentication: Sign up, log in, log out
Add, view, and delete notes
Database models using SQLAlchemy ORM
Secure password storage using werkzeug.security
Dynamic content rendering using Flask templates


Prerequisites
Before you begin, ensure you have met the following requirements:

Python 3.7+
Flask 2.x
MySQL or SQLite for local development
MySQL connector or SQLite connector installed


Installation

Flask Notes App
This is a basic web application built using Flask, allowing users to sign up, log in, and create notes. The application supports user authentication using flask-login and handles CRUD operations for notes using SQLAlchemy ORM.

Features
User authentication: Sign up, log in, log out
Add, view, and delete notes
Database models using SQLAlchemy ORM
Secure password storage using werkzeug.security
Dynamic content rendering using Flask templates
Prerequisites
Before you begin, ensure you have met the following requirements:

Python 3.7+
Flask 2.x
MySQL or SQLite for local development
MySQL connector or SQLite connector installed


Installation

1. Clone the repository:
git clone <repository_url>
cd <repository_directory>

2. Create a virtual environment and activate it:

# On Linux/Mac
python3 -m venv venv
source venv/bin/activate

# On Windows
python -m venv venv
venv\Scripts\activate

3. Install the required dependencies:


4. Set up your database:
Update your database configuration in website/__init__.py. If using MySQL, configure it like:
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://username:password@localhost/database_name'


5. Initialize the database:

flask shell
>>> from website import db
>>> db.create_all()

6. Run the app:

flask --app main run
