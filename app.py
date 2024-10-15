from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config
from src.routes.userRoutes import usuario_blueprint
from src.models.user import db  

def create_app():
    app = Flask(__name__)
    app.config.from_object(config['development'])
    db.init_app(app) 
    app.register_blueprint(usuario_blueprint)
    return app

if __name__ == '__main__':
    app = create_app()  # Crea la app aquí
    app.run(debug=True)
