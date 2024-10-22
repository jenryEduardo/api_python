from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os


load_dotenv()

db=SQLAlchemy()



class Hoja_enfermeria(db.Model):
    name_schema=os.getenv('DATABASE_URL')
    __nameTable__='tablaEnfermeria'
    __tabla_args__=('SCHEMA',name_schema)

    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(45),nullable=False)
    edad=db.Column(db.Integer,nullable=False)

    def __init__(self,id,name,edad):
        self.id=id
        self.name=name
        self.edad=edad

