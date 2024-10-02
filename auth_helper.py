import jwt
from datetime import datetime, timedelta
from config import API_SECRET_KEY

ACCESS_TOKEN_LIFETIME = datetime.now() + timedelta(minutes=30)
REFRESH_TOKEN_LIFETIME = datetime.now() + timedelta(days=1)
JWT_ALGORITHM = "HS512"


def get_authentication_tokens(user):
    access_token = jwt.encode({
        'id': user.id,
        'exp' : ACCESS_TOKEN_LIFETIME,
        "type": "access"
        }, API_SECRET_KEY, algorithm=JWT_ALGORITHM)

    refresh_token = jwt.encode({
        'id': user.id,
        'exp' : REFRESH_TOKEN_LIFETIME,
        "type": "access"
        }, API_SECRET_KEY, algorithm=JWT_ALGORITHM)

    return {
        "access_token": access_token,
        "refresh_token": refresh_token,
        "access_token_expiry": ACCESS_TOKEN_LIFETIME,
        "refresh_token_expiry": REFRESH_TOKEN_LIFETIME
    }
