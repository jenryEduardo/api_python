from flask import jsonify, request
from src.models.user import User, db
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
import bcrypt
from datetime import timedelta


def crear_usuario():
    data = request.get_json()
    
    rol = data.get('rol')
    nombre = data.get('nombre')
    apellido = data.get('apellido')
    email = data.get('email')
    contra = data.get('contra')
    num_tel = data.get('num_tel')

    # Verificar si el email ya está registrado
    if User.query.filter_by(email=email).first():
        return jsonify({"mensaje": "El email ya está registrado"}), 400

    # Hashear la contraseña
    hashed_password = bcrypt.hashpw(contra.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    # Crear el nuevo usuario con la contraseña hasheada
    nuevo_usuario = User(rol=rol, nombre=nombre, apellido=apellido, email=email, contra=hashed_password, num_tel=num_tel)
    
    db.session.add(nuevo_usuario)
    db.session.commit()

    return jsonify({
        "mensaje": "Usuario creado con éxito",
        "id_user": nuevo_usuario.id_user,
        "nombre": nuevo_usuario.nombre,
        "email": nuevo_usuario.email
    }), 201


def login_usuario():
    data = request.get_json()
    email = data.get('email')
    passw = data.get('contra')

    user = User.query.filter_by(email=email).first()

    # print(user.nombre.value)

    if not user or not bcrypt.checkpw(passw.encode('utf-8'), user.contra.encode('utf-8')):
        return jsonify({"mensaje": "Credenciales inválidas"}), 401

    access_token = create_access_token(identity=user.id_user, expires_delta=timedelta(hours=10))
    return jsonify({"mensaje": "Inicio de sesión exitoso", "token": access_token,"rol":user.rol.value,"nombre":user.nombre}), 200



def obtener_usuario():
        # Obtener todos los usuarios
        users = User.query.all()

        # Verificar si no hay usuarios en la base de datos
        if not users:
            return jsonify({
                "success": False,
                "message": "No se encontraron registros"
            }), 404  # Respondemos con un código 404 si no se encuentran registros

        # Formatear los datos en una lista de diccionarios
        users_list = [
            {
                "id_user": user.id_user,
                "rol": user.rol.value,  # Convertir el enum a su valor
                "nombre": user.nombre,
                "apellido": user.apellido,
                "email": user.email,
                "num_tel": user.num_tel
            }
            for user in users
        ]

        # Respuesta exitosa con los datos de los usuarios
        return jsonify({
            "success": True,
            "data": users_list
        }), 200  # Código de éxito



@jwt_required()
def eliminar_usuario(user_id):
    user = User.query.get(user_id)

    if not user:
        return jsonify({"mensaje": "Usuario no encontrado"}), 404

    db.session.delete(user)
    db.session.commit()

    return jsonify({"mensaje": "Usuario eliminado exitosamente"}), 200


@jwt_required()
def editar_usuario(user_id):
    
    user = User.query.get(user_id)

    if not user:
        return jsonify({"mensaje": "Usuario no encontrado"}), 404


    data = request.get_json()
    
  
    user.rol = data.get('rol', user.rol)
    user.nombre = data.get('nombre', user.nombre)
    user.apellido = data.get('apellido', user.apellido)
    user.email = data.get('email', user.email)
    user.num_tel = data.get('num_tel', user.num_tel)

  
    nueva_contra = data.get('contra')
    if nueva_contra:
        user.contra = bcrypt.hashpw(nueva_contra.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    db.session.commit()

    return jsonify({
        "mensaje": "Usuario actualizado exitosamente",
        "id_user": user.id_user,
        "nombre": user.nombre,
        "email": user.email,
        "rol": user.rol.value  
    }), 200
