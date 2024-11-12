from flask import Blueprint
from src.controllers.doctorController import crear_doctor, login_doctor, obtener_doctor, eliminar_doctor,editar_doctor

doctor_blueprint = Blueprint('doctores', __name__)

@doctor_blueprint.route('/doctors', methods=['POST'])
def crear_doctor_ruta():
    return crear_doctor()


@doctor_blueprint.route('/doctors/login', methods=['POST'])
def login_doctor_ruta():
    return login_doctor()

@doctor_blueprint.route('/edit',methods=['PUT'])
def edit_doctor(id_doctor):
    return editar_doctor(id_doctor)

@doctor_blueprint.route('/doctors/profile', methods=['GET'])
def obtener_doctor_ruta():
    return obtener_doctor()  

# Ruta para eliminar un doctor por su ID
@doctor_blueprint.route('/doctors/<int:doctor_id>', methods=['DELETE'])
def eliminar_doctor_ruta(doctor_id):
    return eliminar_doctor(doctor_id)
