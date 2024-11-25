from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from config import config
from src.routes.userRoutes import usuario_blueprint
from flask_cors import CORS
from src.models.user import db

def create_app():
    app = Flask(__name__)     
    CORS(app, resources={
        r"/usuarios/*": {
            "origins": "*",
            "methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"],
            "allow_headers": ["Content-Type", "Authorization"]
        }
    })

    app.config.from_object(config['development'])
    db.init_app(app)
    jwt = JWTManager(app)
    app.register_blueprint(usuario_blueprint)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
