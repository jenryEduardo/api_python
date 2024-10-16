import os
from dotenv import load_dotenv

load_dotenv()  

class Config:
    # Carga la URI de la base de datos y la clave secreta para JWT desde las variables de entorno
    #DATABASE_URL = postgresql://user:password@localhost/database
    #JWT_SECRET_KEY = 'PALABRA_SECRETAÑ'
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')

config = {
    'development': Config,
    'testing': Config
}
