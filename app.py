from flask_openapi3 import Info
from flask_openapi3 import OpenAPI
from db_connection import db

from flask_migrate import Migrate

from auth import auth_bp

jwt = {
    "type": "http",
    "scheme": "bearer",
    "bearerFormat": "JWT"
}
security_schemes = {"jwt": jwt}

def create_app():
    info = Info(title='API Documentation', version='0.0.0.1')
    app = OpenAPI(__name__, info=info, security_schemes=security_schemes)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost:3306/test_flask'

    app.register_api(auth_bp)
    db.init_app(app)

    Migrate(app, db)

    return app
