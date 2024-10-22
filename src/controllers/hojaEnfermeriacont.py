from src.models.hoja_enfermeria import Hoja_enfermeria,db


def agregarHoja(data):
    id=data.get('id')
    name=data.get('name')
    edad=data.get('edad')

    nuevaHoja=Hoja_enfermeria(id=id,name=name,edad=edad)
    db.session.add(nuevaHoja)
    db.session.commit()

    