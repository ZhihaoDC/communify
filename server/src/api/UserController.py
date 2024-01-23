from flask import request, Blueprint, session
from flask.json import jsonify
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
from datetime import datetime, timedelta
from src import app_config
from src.models.UserModel import User
from src.services import UserService

UserController = Blueprint('UserController', __name__)

SESSION_TIME = 30


@UserController.route('/create-user', methods=['POST'])
def sign_up():
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    #Check if user exists
    existing_user = UserService.get_by_email(User, email=email)
    if existing_user: 
        return jsonify({
            'errorMessage': 'User already exists'
        }), 409
    
    created_user = UserService.add_instance(User,
                                            username=username,
                                            email=email,
                                            password=generate_password_hash(password, method='sha256'))
    #Login user
    token = jwt.encode({'sub': created_user['email'],
                        'iat': datetime.utcnow(),
                        'exp': datetime.utcnow() + timedelta(minutes=SESSION_TIME)},
                        app_config.SECRET_KEY)

    return jsonify({'user': created_user, 
                    'jwt': token,
                    'successMsg': f'User {created_user["username"]} created.'
                    }), 200
    

@UserController.route('/login', methods=['POST'])
def login():
    data = request.get_json()

    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    import sys

    if username:
        user = UserService.get_by_username(User, username)
        # print(user, file=sys.stderr)
    if email:
        user = UserService.get_by_email(User, email)
        print(user, file=sys.stderr)
        
    if not user:
        return jsonify({'errorMessage': 'User not found'}), 404

    is_password_correct = check_password_hash(user['password'], password)

    #Unsuccessful login
    if not user or not is_password_correct:
        return {'message': 'Invalid token. Registeration and / or authentication required',
                        'status': 401,
                        'authenticated': False
                        }, 401
    
    #Successful login
    token = jwt.encode({'sub': user['email'],
                        'iat': datetime.utcnow(),
                        'exp': datetime.utcnow() + timedelta(minutes=SESSION_TIME)
                        },
                        app_config.SECRET_KEY)
    return jsonify({'user': user, 
                    'jwt': token,
                    'successMsg': f'User {user["username"]} successfully logged in.'
                    }), 200