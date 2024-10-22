from flask_sqlalchemy import SQLAlchemy
from dotenv import  load_dotenv
import os

load_dotenv()

db=SQLAlchemy()

class Paciente(db.Model):
    schemaname=os.getenv('DATABASE_URL')
    __tablename__='Paciente'
    __tableargs__={'SCHEMA':schemaname}

    name=db.column(db.String(45),nullable=True)

    def __init__(self,name):
        self.name=name