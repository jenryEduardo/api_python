from flask import Blueprint, request
from src.controllers.userController import crear_usuario

usuario_blueprint = Blueprint('usuarios', __name__)

@usuario_blueprint.route('/users', methods=['POST'])
def crear_usuario_ruta():
    data = request.get_json()
    
    return crear_usuario(data)
