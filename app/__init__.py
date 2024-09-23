from flask_openapi3 import Info
from flask_openapi3 import OpenAPI
from .views.auth import auth_bp, login, signup


info = Info(title='API Documentation', version='0.0.0.1')
app = OpenAPI(__name__, info=info)

app.register_api(auth_bp)
auth_bp.register_blueprint(login)
auth_bp.register_blueprint(signup)


if __name__ == '__main__':
    app.run(debug=True)