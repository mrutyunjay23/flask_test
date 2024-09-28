import jwt
from datetime import datetime, timedelta
from flask import session, request
from flask_openapi3 import APIBlueprint
from pydantic import BaseModel, Field
from flask_openapi3 import Tag


from models import UserModel
from db_connection import db

from config import API_SECRET_KEY

security = [{"jwt": []}]

auth_bp = APIBlueprint('auth', __name__, url_prefix='/auth', abp_security=security,)


# @auth_bp.before_app_request
# def load_logged_in_user():
#     user_id = session.get('user_id')

#     if user_id is None:
#         g.user = None
#     else:
#         g.user = UserModel.query.get(user_id)


# @auth_bp.route('/logout')
# def logout():
#     session.clear()
#     return {
#             "code": 200,
#             "message": "Logged out"
#             }


# def login_required(view):
#     @functools.wraps(view)
#     def wrapped_view(**kwargs):
#         if g.user is None:
#             return 'wrong pass'

#         return view(**kwargs)

#     return wrapped_view


login_tags = Tag(name='login-post', description='Customer Login API')

class LoginBody(BaseModel):
    email: str = Field(..., min_length=2, max_length=30, description='email')
    password: str = Field(None, min_length=2, max_length=50, description='password')

@auth_bp.post('/login', tags=[login_tags])
def login(body: LoginBody):
    """Login to test application
    """

    user = UserModel.query.filter_by(email=body.email).first()
    if user and user.authenticate(body.password):
        token = jwt.encode({
            'id': user.id,
            'exp' : datetime.now() + timedelta(minutes = 30)
            }, API_SECRET_KEY)
        return {
        "code": 200,
        "token": token
        }
    else:
        return {
            "code": 200,
            "message": "Incorrect password",
            "data": {"name": body.email}
            }


signup_tag = Tag(name='signup-post', description='Signup request')

class SignupBody(BaseModel):
    name: str
    password: str
    email: str
    address: str


@auth_bp.post('/signup', tags=[signup_tag])
def signup(body: SignupBody):
    """Sign up to test application
    """

    user = UserModel(name=body.name, email=body.email, address=body.address)
    user.password_hash = body.password
    db.session.add(user)
    db.session.commit()

    return {
        "code": 200,
        "message": "ok",
        "data": {
            "name": user.name,
            "email": user.email,
            "address": user.address
        }
    }


get_all_users = Tag(name='get-users', description='get_all_users')

@auth_bp.get('/get-users', tags=[get_all_users])
def get_users():
    """Sign up to test application
    """
    print(request.headers.get('Authorization'))

    user_object = UserModel.query.all()

    users = [user.to_dict() for user in user_object]

    return {
        "code": 200,
        "message": "ok",
        "data": users
    }
