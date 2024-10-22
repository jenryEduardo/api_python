from flask import Blueprint,request
from src.controllers.pacientecontroller import agregarPaciente

pablueprint=Blueprint('paciente',__name__)

@pablueprint.route('addPaciente',methods=['POST'])
def agregarparoute():
    data=request.get_json()
    agregarPaciente(data)