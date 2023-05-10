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

    name = request.json.get('name')
    username = request.json.get('username')
    password = request.json.get('password')
    if username and password:
        user = User.create(name,username, password)
        return 'Registration succcessful', 200
    return 'Username and Password Required', 400