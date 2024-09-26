from flask_openapi3 import APIBlueprint

from pydantic import BaseModel, Field

from flask_openapi3 import Tag

from models import UserModel
from db_connection import db


auth_bp = APIBlueprint('auth', __name__, url_prefix='/auth')

login_tags = Tag(name='login-post', description='Customer Login API')

class LoginBody(BaseModel):
    name: str = Field(..., min_length=2, max_length=6, description='username')
    password: str = Field(None, min_length=2, max_length=8, description='password')

@auth_bp.post('/login', tags=[login_tags])
def login(body: LoginBody):
    """Login to test application
    """
    return {
        "code": 200,
        "message": "ok",
        "data": {"bid": 1, "name": body.name, "password": body.password}
    }


signup_tag = Tag(name='signup-post', description='Signup request')

class SignupBody(BaseModel):
    id: int
    name: str
    password: str
    email: str
    address: str


@auth_bp.post('/signup', tags=[signup_tag])
def signup(body: SignupBody):
    """Sign up to test application
    """

    user = UserModel(id=body.id, name=body.name, password=body.password, email=body.email, address=body.email)
    db.session.add(user)
    db.session.commit()

    
    return {
        "code": 200,
        "message": "ok",
        "data": {
            "id": user.id,
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

    user_object = UserModel.query.all()

    print(type(user_object[0]))

    users = [user.to_dict() for user in user_object]

    return {
        "code": 200,
        "message": "ok",
        "data": users
    }
