from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from dotenv import load_dotenv
from sqlalchemy import Enum
import enum
import os

# Inicialización de SQLAlchemy y Bcrypt
db = SQLAlchemy()
bcrypt = Bcrypt()
load_dotenv()


class RolEnum(enum.Enum):
    admin="admin"
    enfermera="enfermera"

# Definición del modelo User
class User(db.Model):
    schema_name = os.getenv('SCHEMA_NAME') 
    __tablename__ = 'users'
    __table_args__ = {'schema': schema_name}

    id_user = db.Column(db.Integer, primary_key=True) 
    rol = db.Column(db.Enum(RolEnum), nullable=False)
    nombre = db.Column(db.String(50), nullable=False)
    apellido=db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    contra = db.Column(db.String(150), nullable=False)
    num_tel=db.Column(db.INTEGER, nullable=False)

    def __init__(self,rol, nombre,apellido, email,contra, num_tel):
        self.rol=rol
        self.nombre = nombre
        self.apellido=apellido
        self.email = email
        self.contra = contra
        self.num_tel=num_tel

    
        consultas = db.relationship('Consulta', backref='User', lazy=True)

    def check_password(self, contra):
        # Usar bcrypt para verificar la contraseña
        return bcrypt.check_password_hash(self.contra, contra)

    def __repr__(self):
        return f'<User {self.nombre}>'
