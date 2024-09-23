from pydantic import BaseModel, Field

from flask_openapi3 import Tag

from . import auth_bp


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
