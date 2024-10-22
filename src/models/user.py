from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from dotenv import load_dotenv
import os

db = SQLAlchemy()
bcrypt = Bcrypt()
load_dotenv()

class User(db.Model):
    schema_name = os.getenv('SCHEMA_NAME') 
    __tablename__ = 'users'
    __table_args__ = {'schema': schema_name}
    
    id_user = db.Column(db.Integer, primary_key=True) 
    nombre = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    
    def __init__(self, nombre, email,id_user):
        self.nombre = nombre
        self.email = email
        self.id_user=id_user
    
    def __repr__(self):
        return f'<User {self.nombre}>'
