from flask import Blueprint
from src.controllers.userController import crear_usuario, login_usuario, obtener_usuario, eliminar_usuario, editar_usuario

usuario_blueprint = Blueprint('/usuarios', __name__, url_prefix='/usuarios')

@usuario_blueprint.route('/users', methods=['POST'])
def crear_usuario_ruta():
    return crear_usuario()  

@usuario_blueprint.route('/login', methods=['POST'])
def login_ruta():
    return login_usuario()  

@usuario_blueprint.route('/profile', methods=['GET'])
def obtener_usuario_ruta():
    return obtener_usuario()  

@usuario_blueprint.route('/users/<int:user_id>', methods=['DELETE'])
def eliminar_usuario_ruta(user_id):
    return eliminar_usuario(user_id)  

@usuario_blueprint.route('/edit/<int:user_id>', methods=['PUT'])  # Cambié id_user por user_id
def edit_user(user_id):  # Cambié id_user por user_id
    return editar_usuario(user_id)
