from db_connection import db

class UserModel(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    password = db.Column(db.String(255))
    email = db.Column(db.String(255))
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
