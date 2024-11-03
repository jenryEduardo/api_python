from flask import Blueprint, request
from src.controllers.doctorController import crear_doctor, obtener_doctor, eliminar_doctor

doctor_blueprint = Blueprint('doctores', __name__)

@doctor_blueprint.route('/doctors', methods=['POST'])
def crear_doctor_ruta():
    return crear_doctor()  # Llama a la función que maneja la creación de doctores

@doctor_blueprint.route('/doctors/<int:doctor_id>', methods=['GET'])
def obtener_doctor_ruta(doctor_id):
    return obtener_doctor(doctor_id)  # Llama a la función que obtiene los datos de un doctor

@doctor_blueprint.route('/doctors/<int:doctor_id>', methods=['DELETE'])
def eliminar_doctor_ruta(doctor_id):
    return eliminar_doctor(doctor_id)  # Llama a la función que maneja la eliminación de un doctor
