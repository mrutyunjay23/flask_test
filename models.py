import bcrypt
import datetime
from db_connection import db
from sqlalchemy.ext.hybrid import hybrid_property



class UserModel(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), unique=True)
    address = db.Column(db.String(255))

    def __repr__(self):
        return f'User with Username-{self.name}'
    
    def to_dict(self):
        """Convert SQLAlchemy object to a dictionary"""
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "address": self.address
        }

    @hybrid_property
    def password_hash(self):
        raise AttributeError('Password hashes may not be viewed.')

    @password_hash.setter
    def password_hash(self, _password):
        password_hash = bcrypt.hashpw(_password.encode('utf-8'), bcrypt.gensalt(14))
        self.password = password_hash.decode('utf-8')   #str

    def authenticate(self, _password):
        return bcrypt.checkpw(_password.encode('utf-8'), self.password.encode('utf-8'))


class AuthTokensModel(db.Model):
    __tablename__ = 'auth_tokens'

    id = db.Column(db.Integer, primary_key=True)
    access_token = db.Column(db.String(500), nullable=True)
    refresh_token = db.Column(db.String(500), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    def __repr__(self):
        return 'Auth tokens'
    
    def to_dict(self):
        """Convert SQLAlchemy object to a dictionary"""
        return {
            "access_token": self.access_token,
            "refresh_token": self.refresh_token,
            "created_at": self.created_at
        }
