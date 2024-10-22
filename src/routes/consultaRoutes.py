from flask import Blueprint, request
from src.controllers.consultaController import crearconsulta

# Crear un Blueprint para las rutas de consulta
consulta_blueprint = Blueprint('consultas', __name__)

# Definir la ruta para crear una consulta
@consulta_blueprint.route('/consultas', methods=['POST'])
def crearConsulta_ruta():
    # Obtener los datos del cuerpo de la solicitud (request)
    data = request.get_json()
    # Llamar a la función crearconsulta y pasar los datos
    return crearconsulta(data)
