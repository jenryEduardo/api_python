from src.models.paciente import Paciente,db
from flask import jsonify


def agregarPaciente(data):
  
    name=data.get('name')

    if not name:
        return jsonify({"error":"tas mal we"})
    
    nuevoPaciente=Paciente(name=name)
    db.session.add(nuevoPaciente)
    db.session.commit()

    return jsonify({
        "test":"agregado con exito"
    })


