from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from sqlalchemy import Enum, Integer, String
import enum
import os

# Inicialización de SQLAlchemy
db = SQLAlchemy()
load_dotenv()

class RolEnum(enum.Enum):
    admin = "admin"
    enfermera = "enfermero"
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

    def __repr__(self):
        return f'<User {self.nombre}>'
