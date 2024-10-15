from flask import request, jsonify
from src.models.user import User, db 

def crear_usuario(data):
    nombre = data.get('nombre')
    email = data.get('email')

    nuevo_usuario = User(nombre=nombre, email=email)

    db.session.add(nuevo_usuario)
    db.session.commit()

    return jsonify({"mensaje": "Usuario creado", "id": nuevo_usuario.id}), 201
