# doctor.py
from sqlalchemy import Column, Integer, String
from src.models.user import User, db
import os
from dotenv import load_dotenv

load_dotenv()

class Doctor(User):
    schema_name = os.getenv('SCHEMA_NAME') 
    __tablename__ = 'doctor'
    __table_args__ = {'schema': schema_name}

    id_doctor = Column(Integer, primary_key=True, autoincrement=True)
    especialidad = Column(String(50), nullable=False)
    num_licencia = Column(String(20), nullable=False)

    def __init__(self, nombre, apellido, email, contra, num_tel, rol, especialidad, num_licencia):
       
        super().__init__(nombre=nombre, apellido=apellido, email=email, contra=contra, num_tel=num_tel, rol=rol)
       
        self.especialidad = especialidad
        self.num_licencia = num_licencia
