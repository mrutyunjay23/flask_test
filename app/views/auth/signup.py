from pydantic import BaseModel, Field

from flask_openapi3 import Tag

from . import auth_bp

signup_tag = Tag(name='signup-post', description='Signup request')

class SignupQuery(BaseModel):
    name: str
    password: str
    email: str
    address: str


@auth_bp.post('/signup', tags=[signup_tag])
def signup(query: SignupQuery):
    """Sign up to test application
    """
    return {
        "code": 200,
        "message": "ok",
        "data": [
            {"bid": 1, "name": query.name, "password": query.password, "email": query.email, "address": query.address},
            {"bid": 1, "name": query.name, "password": query.password, "email": query.email, "address": query.address}
        ]
    }
