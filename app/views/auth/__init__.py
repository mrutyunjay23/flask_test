from flask_openapi3 import APIBlueprint

auth_bp = APIBlueprint('auth', __name__, url_prefix='/auth')