from flask import Blueprint,request
from src.controllers.hojaEnfermeriacont import agregarHoja

hojablueprint=Blueprint('Hoja',__name__)

@hojablueprint.route('hojaAdd',methods=['POST'])
def hojaAgregar():
    data=request.get_json()
    agregarHoja(data)