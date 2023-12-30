from flask import request, Blueprint, session
from flask.json import jsonify
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
from datetime import datetime, timedelta
from src import app_config
from src.models.UserModel import User
from src.services import UserService

UserController = Blueprint('UserController', __name__)

@UserController.route('/create-user', methods=['POST'])
def sign_up():
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    #Check if user exists
    user = UserService.get_by_email(User, email=email)
    if user: 
        return jsonify({
            'errorMessage': 'User already exists'
        }), 400
    
    created_user = UserService.add_instance(User,
                                            username=username,
                                            email=email,
                                            password=generate_password_hash(password, method='sha256'))
    
    return jsonify({
        'successMsg': f'User {created_user["username"]} created.'
    }), 200
    

@UserController.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    email = request.form.get('email')
    password = request.form.get('password')

    #Check user
    user = UserService.get_by_email(email)
    is_password_correct = check_password_hash(user.password, password)
    if not user or not is_password_correct:
        return jsonify({'errorMessage': 'Wrong password', 'authenticated': False}), 401
    
    token = jwt.encode({
        'sub': user['id'],
        'iat': datetime.utcnow(),
        'exp': datetime.utcnow() + timedelta(minutes=30)},
        app_config['SECRET_KEY']

    )
    return jsonify({'successMsg': 'User logged in'}, token.decode('UTF-8')), 200

