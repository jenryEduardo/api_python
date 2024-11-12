# user.py
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from dotenv import load_dotenv
from sqlalchemy import Enum, Integer, String
import enum
import os

# Inicialización de SQLAlchemy y Bcrypt
db = SQLAlchemy()
bcrypt = Bcrypt()
load_dotenv()

class RolEnum(enum.Enum):
    admin = "admin"
    enfermera = "enfermera"
    doctor = "doctor"

# Definición del modelo User
class User(db.Model):
    schema_name = os.getenv('SCHEMA_NAME') 
    __tablename__ = 'users'
    __table_args__ = {'schema': schema_name}

    id_user = db.Column(Integer, primary_key=True)  # Cambié a `id` para que coincida con el modelo `Doctor`
    rol = db.Column(Enum(RolEnum), nullable=False)
    nombre = db.Column(String(50), nullable=False)
    apellido = db.Column(String(50), nullable=False)
    email = db.Column(String(100), nullable=False, unique=True)
    contra = db.Column(String(150), nullable=False)
    num_tel = db.Column(Integer, nullable=False)
    
    # consultas = db.relationship('Consulta', backref='user', lazy=True)

    def __init__(self, rol, nombre, apellido, email, contra, num_tel):
        self.rol = rol
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.contra = bcrypt.generate_password_hash(contra).decode('utf-8')
        self.num_tel = num_tel

    def check_password(self, contra):
        # Usar bcrypt para verificar la contraseña
        return bcrypt.check_password_hash(self.contra, contra)

    def __repr__(self):
        return f'<User {self.nombre}>'
