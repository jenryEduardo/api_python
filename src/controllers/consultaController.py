from src.models.consulta import Consulta, db


def crearconsulta(data):
    id_consulta=data.get('id_consulta')
    nombre_paciente=data.get('nombre_paciente')
    sintomas=data.get('sintomas')
    
    nueva_consulta=Consulta(id_consulta=id_consulta,nombre_paciente=nombre_paciente,sintomas=sintomas)
    db.session.add(nueva_consulta)
    db.session.commit()
    