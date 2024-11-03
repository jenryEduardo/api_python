from flask import jsonify, request
from src.models.doctor import Doctor, db  # Asegúrate de importar la clase Doctor
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
import bcrypt
from dotenv import load_dotenv

load_dotenv()

@jwt_required()
def crear_doctor():
    data = request.get_json()

    nombre = data.get('nombre')
    apellido = data.get('apellido')
    email = data.get('email')
    contra = data.get('contra')
    num_tel = data.get('num_tel')
    rol = data.get('rol')
    especialidad = data.get('especialidad')
    num_licencia = data.get('num_licencia')

    # Verificar si el email ya está registrado
    if Doctor.query.filter_by(email=email).first():
        return jsonify({"mensaje": "El email ya está registrado"}), 400

    # Hashear la contraseña
    hashed_password = bcrypt.hashpw(contra.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    # Crear el nuevo doctor
    nuevo_doctor = Doctor(
        nombre=nombre,
        apellido=apellido,
        email=email,
        contra=hashed_password,
        num_tel=num_tel,
        rol=rol,
        especialidad=especialidad,
        num_licencia=num_licencia
    )
    
    db.session.add(nuevo_doctor)
    db.session.commit()

    return jsonify({
        "mensaje": "Doctor creado con éxito",
        "id_doctor": nuevo_doctor.id_doctor,
        "nombre": nuevo_doctor.nombre,
        "email": nuevo_doctor.email
    }), 201

@jwt_required()
def login_doctor():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    doctor = Doctor.query.filter_by(email=email).first()

    if not doctor or not bcrypt.checkpw(password.encode('utf-8'), doctor.contra.encode('utf-8')):
        return jsonify({"mensaje": "Credenciales inválidas"}), 401

    access_token = create_access_token(identity=doctor.id_doctor)
    return jsonify({"mensaje": "Inicio de sesión exitoso", "token": access_token}), 200

@jwt_required()
def obtener_doctor():
    doctor_id = get_jwt_identity()
    doctor = Doctor.query.get(doctor_id)

    if not doctor:
        return jsonify({"mensaje": "Doctor no encontrado"}), 404

    return jsonify({
        "id_doctor": doctor.id_doctor,
        "nombre": doctor.nombre,
        "email": doctor.email,
        "especialidad": doctor.especialidad,
        "num_licencia": doctor.num_licencia
    }), 200

@jwt_required()
def eliminar_doctor(doctor_id):
    doctor = Doctor.query.get(doctor_id)

    if not doctor:
        return jsonify({"mensaje": "Doctor no encontrado"}), 404

    db.session.delete(doctor)
    db.session.commit()

    return jsonify({"mensaje": "Doctor eliminado exitosamente"}), 200
