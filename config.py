import os
from dotenv import load_dotenv

load_dotenv() 

class Config:
    #DATABASE_URL=postgresql://user:pwd@localhost:5432/bd_name
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

config = {
    'development': Config,
    'testing': Config
}