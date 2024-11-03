# doctor.py
from sqlalchemy import Column, Integer, String
from src.models.user import User, db

class Doctor(User):
    __tablename__ = 'doctors'

    # Definimos los campos específicos de Doctor
    id_doctor = Column(Integer, primary_key=True, autoincrement=True)
    especialidad = Column(String(50), nullable=False)
    num_licencia = Column(String(20), nullable=False)

    def __init__(self, nombre, apellido, email, contra, num_tel, rol, especialidad, num_licencia):
        # Llamamos al constructor de la clase base User
        super().__init__(nombre=nombre, apellido=apellido, email=email, contra=contra, num_tel=num_tel, rol=rol)
        
        # Asignamos los atributos específicos de Doctor
        self.especialidad = especialidad
        self.num_licencia = num_licencia
