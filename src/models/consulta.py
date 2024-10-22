from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os

load_dotenv()
db=SQLAlchemy()

class Consulta(db.Model):
    schema_name=os.getenv('DATABASE_URL')
    __tablename__='consultas'
    __tableargs__={'SCHEMA',schema_name}

id_consulta=db.Column(db.Integer, primary_key=True)
nombre_paciente= db.Column(db.string(45), nullable=False)
sintomas=db.Column(db.String(100), nullable=False)

def __init__(self, id_consulta,nombre_paciente, sintomas):
    self.id_consulta=id_consulta
    self.nombre_paciente=nombre_paciente
    self.sintomas=sintomas
