from flask import jsonify, request
from src.models.user import User, db
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
import bcrypt
from dotenv import load_dotenv

load_dotenv()

@jwt_required()
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

@jwt_required()
def login_usuario():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    user = User.query.filter_by(email=email).first()

    if not user or not bcrypt.checkpw(password.encode('utf-8'), user.contra.encode('utf-8')):
        return jsonify({"mensaje": "Credenciales inválidas"}), 401

    access_token = create_access_token(identity=user.id_user)
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
