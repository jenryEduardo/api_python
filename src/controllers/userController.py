from flask import jsonify, request
from src.models.user import User, db
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
import bcrypt
from dotenv import load_dotenv
from datetime import timedelta

load_dotenv()


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

    # Crear el nuevo usuario
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
    password = data.get('contra')
    user = User.query.filter_by(email=email).first()

    if not user or not bcrypt.checkpw(password.encode('utf-8'), user.contra.encode('utf-8')):
        return jsonify({"mensaje": "Credenciales inválidas"}), 401

    access_token = create_access_token(identity=user.id_user,expires_delta=timedelta(hours=10))
    return jsonify({"mensaje": "Inicio de sesión exitoso", "token": access_token}), 200

@jwt_required()
def obtener_usuario():
    user_id = get_jwt_identity()
    user = User.query.get(user_id)

    if not user:
        return jsonify({"mensaje": "Usuario no encontrado"}), 404

    return jsonify({
        "id_user": user.id_user,
        "nombre": user.nombre,
        "email": user.email
    }), 200

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
