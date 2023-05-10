#step 1
create .env file, config.py, run.py

#step 2 
create a folder App

#step 3
create a file in the app ___init__.py

#step 4 
In run.py, run your app using the following: 
from app import app

if __name__ == "__main__":
    app.run()

#step 5
In .env file, enter the following:
DATABASE_URL=postgresql:///practical_db
SECRET_KEY=someserioussecret

#step 6
in the config.py, import os and the write the following:

SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')

#step 7
create virtual environment and activate

#step 8
make all necesarry installations:
flask
marshmallow
migrate
flask sqlalchemy

#step 9
in the __init__.py file, do the following:
from flask import Flask

app = Flask(__name__)

@app.get('/')
def index():
    return "Welcome to our app"

#step 6
In thunderclient, test to see if index endpoint is working first by running flask... 
NB:it required the following;  There are .env or .flaskenv files present. Do "pip install python-dotenv" to use them.

#step 7
add the importations of sqlachemy,marshmallow and migrate to the __init__.py file while including config files:

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
import os 

app = Flask(__name__)
app.config.from_object('config')
app.secret_key=os.environ.get('SECRET_KEY')
db = SQLAlchemy(app)
ma = Marshmallow(app)
migrate = Migrate(app, db)


#step 8
create a database in postgresql and give it a name from the name in the .env file... in this case, practical_db

#step 9 
create a folder inside app folder and call it user, and inside the user folder, create three files...one for endpoints,database and schema each(controller,model and schema). Inside user, create an __init__.py file

#step 10
in the model.py, create a model...start by importing db from app
then create functions that will be used to save,update,set and validate password,then create a class method that will be accessed in the controller

#step 11
create blueprint and routes by doing the following:
from flask import Blueprint,request

from app.user.model import User

user = Blueprint("user",__name__,url_prefix="/user")


@user.post('/login')
def login():
    username = request.json.get('username')
    password = request.json.get('password')
    if username and password:
        user = User.get_by_username(username)
        if user and user.is_valid(password):
            return 'Login succcessful'
    return 'User not found', 401

@user.post('/register')
def register():
    username = request.json.get('username')
    password = request.json.get('password')
    if username and password:
        user = User.create(username, password)
        return 'Registration succcessful', 200
    return 'Username and Password Required', 400

#step 12
register blueprint in the __init__.py file;
from app.user.controller import user
app.register_blueprint(user)

#step 13
run pip install psycopg2-binary then,
run $flask db init, $flask db migrate -m "Initial migration" and $flask db upgrade in terminal then run using "flask run --debug" and test with thunder client


#corrections
1. used a wrong port which was changes
2. didnt add name which was not nullable which i added to the cls
3. needed to check password before saving